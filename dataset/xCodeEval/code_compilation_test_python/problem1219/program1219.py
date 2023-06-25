    """
    Author: Nikhil Tripathi
    Date Created: 5th September,2018
    Part of project: OCI AUTOMATION
    Description: The following python script automates the flow of Ecra installation in the oci environment along with
    adding the cabinet,composing the cluster,provisioning a service on the cluster,creating starter db followed by pod
    creation inside the domU through rest api calls.
    
    This script is meant to be run from the R1 bastion host and requires the following input from the user:
    
      *ecra_host ---------------------------------------------The ecra host in which the ecra installation needs to be done(ecra-host1 or ecra-host2)
      *dir_name ----------------------------------------------The root directory in which the ecra needs to be installed
      *ecra_name ---------------------------------------------The name of the installed ecra
      *cluster_name-------------------------------------------The cluster which needs to be provisioned
      *label_name---------------------------------------------The label corresponding to which the ecra needs to be installed
    """
    
    
    
    import sys
    import os
    import subprocess
    import json
    import time
    import multiprocessing
    
    from subprocess import call
    
    
    class OciAutomation:
    
    
    def __init__(self, ecra_host, dir_name, ecra_name, cluster_name, label_name):
            self.ecra_host = ecra_host
            self.dir_name = dir_name
            self.cluster_name = cluster_name
            self.ecra_name = ecra_name
            self.label_name = label_name
            OciAutomation.ecra_root = '/' + dir_name + '/oracle/ecra_installs/' + str(ecra_name) + '/'
            OciAutomation.exacloud_root = OciAutomation.ecra_root + 'mw_home/user_projects/domains/exacloud' + '/'
    
        #file_path must include the absolute path of the file
    def install_completed(file_path, pattern, host):
            result = 1
            while result != 0:
                COMMAND = """
                             grep """+ pattern +' '+ file_path +"""      
                         """
    
                detecting_pattern = subprocess.Popen(["ssh", "-i", "./dbaas_sshkey.priv", "%s" % host, COMMAND],
                                                      shell=False,
                                                      stdout=subprocess.PIPE,
                                                      stderr=subprocess.PIPE)
                detecting_pattern.wait()
    
                result = detecting_pattern.stdout.readlines()
                detecting_pattern.terminate()
                time.sleep(60)
            return result
    
    def killIfAlive( process):
            if process.is_alive():
                process.terminate()
                sys.exit("Script terminated due to failure in service creation or ecra installation...")
    
    
    
    def parameter_calculation(self):
            #compute path to the flat file and the payload.json file from the cluster name
            OciAutomation.cluster_type = '220' if self.cluster_name.find('220') else ('214' if self.cluster_name.find('214') else '410')
    
            #since 410 would have 3 clusters,for provisioning the service cluster number would be required
            #for 220 and 214 always the second cluster(03-04) is provisioned
            if '01-02' in cluster_name:
                OciAutomation.cluster_number = 'c1'
                OciAutomation.compose_count = 1
            elif '03-04' in cluster_name:
                OciAutomation.cluster_number = 'c2'
                OciAutomation.compose_count = 2
    
            elif '05-06' in cluster_name:
                OciAutomation.cluster_number = 'c3'
                OciAutomation.compose_count = 3
    
            self.ecra_host = 'opc@10.0.1.3' if self.ecra_host is 1 else 'opc@10.0.1.5'
    
    
    def fetch_flatfile_payload_json_details(self):
    
            path_to_flat_file_directory = '/ecra_sw/important_files/cabinet_'+OciAutomation.cluster_type+'_files/'
            COMMAND ="""
                    cd """+path_to_flat_file_directory+"""
                    ls | grep flatfile
                    
            """
            flat_file = subprocess.Popen(["ssh","-i","./dbaas_sshkey.priv", "%s" % self.ecra_host, COMMAND],
                                   shell=False,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            flat_file.wait()
            OciAutomation.flat_file = path_to_flat_file_directory + str(flat_file.stdout.readlines())
    
            if not OciAutomation.flat_file:
                error = flat_file.stderr.readlines()
                print >>sys.stderr, "ERROR: %s" % error
                sys.exit()
            else:
                print OciAutomation.flat_file
    
            COMMAND = """
                    cd """ + path_to_flat_file_directory + """
                    ls | grep """+OciAutomation.cluster_number+'_410.json'+"""
            
            """ if cluster_type is '410' \
                else """
                    cd """ + path_to_flat_file_directory + """
                    ls | grep """+'payload.json'+"""
            
            """
            payload_json_file = subprocess.Popen(["ssh", "-i", "./dbaas_sshkey.priv", "%s" % self.ecra_host, COMMAND],
                                             shell=False,
                                             stdout=subprocess.PIPE,
                                             stderr=subprocess.PIPE)
            payload_json_file.wait()
            OciAutomation.payload_json_file = payload_json_file.stdout.readlines()
            if not OciAutomation.payload_json_file:
                error = payload_json_file.stderr.readlines()
                print >>sys.stderr, "ERROR: %s" % error
                sys.exit()
            else:
                print OciAutomation.payload_json_file
    
    
        #The following method downloads the required tar files from the oss container,concats them and untars the merged file(ecra-full.tar)
    def download_tarfile( self, file_name):
            URL = 'https://swiftobjectstorage.us-phoenix-1.oraclecloud.com/v1/intdbaasecra/LargeFilesDisposableAfterUse/'
            oss_list = subprocess.Popen(["curl", "-u", "ravindranath.chennoju@oracle.com:DdxA2#tz6IA:}V]xjE(W",
                                     "https://swiftobjectstorage.us-phoenix-1.oraclecloud.com/v1/intdbaasecra/LargeFilesDisposableAfterUse/"],
                                    stdout=subprocess.PIPE).communicate()[0]
            oss_files = json.loads(oss_list)
            label_files = []
            for x in oss_files:
                if file_name in x['name']:
                    label_files.append(x['name'])
    
            #Dowloading the files in the label_files list from the OSS container
            COMMAND = """
                     cd /"""+self.dir_name+"""       
                 """
    
            for x in label_files:
                COMMAND+="""
                     curl -u ravindranath.chennoju@oracle.com:'DdxA2#tz6IA:}V]xjE(W' -X GET -O"""+URL+str(x)+"""
                """
    
            download_tar_files = subprocess.Popen(["ssh", "-i", "./dbaas_sshkey.priv", "%s" % self.ecra_host, COMMAND],
                                   shell=False,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            download_tar_files.wait()
            result = download_tar_files.stdout.readlines()
            if not result:
                error = download_tar_files.stderr.readlines()
                print >>sys.stderr, "ERROR: %s" % error
                sys.exit()
            else:
                print result
    
            #concatenating the tar files present in the directory in a single ecra-full.tar and untar it
            COMMAND="""
                   cd /"""+ self.dir_name +"""
                   cat *.tar > ecra-full.tar
                   tar xvf ecra-full.tar
            """
            concat_files = subprocess.Popen(["ssh", "-i", "./dbaas_sshkey.priv", "%s" % self.ecra_host, COMMAND],
                                   shell=False,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            concat_files.wait()
            result = concat_files.stdout.readlines()
            if not result:
                error = concat_files.stderr.readlines()
                print >> sys.stderr, "ERROR: %s" % error
            else:
                printresult
    
            print "File untarred succesfully"
    
    
    def edit_deployment_json_file(self):
        # we need to modify the deployment.json file for the oci env
            file_path = self.dir_name+'/oracle/ecra_installs/'+self.ecra_name+'/ecradpy/package/config/diagnostic/'
    
            COMMAND = """
                    cd /""" + file_path + """
                    jq -c '.deployment.dest =""" + dir_name + """"' test.json > tmp.$$.json && mv tmp.$$.json test.json
            """
            edit_deployment_json = subprocess.Popen(["ssh", "-i", "./dbaas_sshkey.priv", "%s" % self.ecra_host, COMMAND],
                                         shell=False,
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE)
            edit_deployment_json.wait()
            result = edit_deployment_json.stdout.readlines()
            if not result :
                error = edit_deployment_json.stderr.readlines()
                print >>sys.stderr, "ERROR: %s" % error
                sys.exit()
            else:
                print result
            print "deployment.json edited successfully!"
    
        #ecra installation comes here
    def install_ecra(self):
            COMMAND = """
                    cd /""" + self.dir_name + """/ecra-full/
                    unzip ecradpy
                    cd ecradpy
                    ./ecradpy --env=bm """+self.ecra_name+"""
            """
            install_ecra = subprocess.Popen(["ssh", "-i", "./dbaas_sshkey.priv", "%s" % self.ecra_host, COMMAND],
                                         shell=False,
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE)
            install_ecra.wait()
            result = install_ecra.stdout.readlines()
            if not result :
                error = install_ecra.stderr.readlines()
                print >>sys.stderr, "ERROR: %s" % error
                sys.exit()
            else:
                print result
    
    def check_ecra_installation_logs(self):
        #checking ecra installation logs for successful completion
            COMMAND = """
                    ls /tmp/ecradpy/log -t | head -n1
            """
            ecra_log_file_fetch = subprocess.Popen(["ssh", "-i", "./dbaas_sshkey.priv", "%s" % self.ecra_host, COMMAND],
                                         shell=False,
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE)
    
            ecra_log_file_fetch.wait()
            result = ecra_log_file_fetch.stdout.readlines()
            if not result :
                error = ecra_log_file_fetch.stderr.readlines()
                print >>sys.stderr, "ERROR: %s" % error
                sys.exit()
            else:
                print result
            log_file_path = '/tmp/ecradpy/' + str(result)
    
            p = multiprocessing.Process(target = install_completed, args= (log_file_path,'Ecra install completed'))
            p.start()
            #wait for ecra installation for 2 hrs(7200 seconds)
            p.join(7200)
    
            killIfAlive(p)
            print "Ecra installation completed successfully!"
    
    
    
        # adding a cabinet
        # the return value of this subprocess will be passed to the compose cluster command as the cell input
    def add_cabinet(self):
            # getting rack_name from the flatfile to know which series cluster do we have
            COMMAND = """
                        grep -q MODEL=X6-2 """+ OciAutomation.flat_file +""" && echo $?
                    """
            getting_cluster_series = subprocess.Popen(["ssh", "-i", "./dbaas_sshkey.priv", "%s" % self.ecra_host, COMMAND],
                                              shell=False,
                                              stdout=subprocess.PIPE,
                                              stderr=subprocess.PIPE)
    
            getting_cluster_series.wait()
            cluster_series = 'X6' if (getting_cluster_series.stdout.readlines() is 0) else 'X7'
            if not cluster_series:
                error = getting_cluster_series.stderr.readlines()
                print >> sys.stderr, "ERROR: %s" % error
                sys.exit()
            else:
                print result
    
            COMMAND = """
                    echo EXADATA_CLOUD_EXACLOUD_REST_USER='admin'
                    echo EXADATA_CLOUD_EXACLOUD_REST_PASSWORD='Welcome1!'
                    cd """+str(OciAutomation.exacloud_root)+'/vcn_cloud'+"""
                    ./cabinets_n_clusters_util.py -i """ + str(OciAutomation.flat_file) + """ -c -s 3cell2comp2ibsw2pdu1ethsw -m """ + str(cluster_series) + """ -d \ 
                    SEA2 --ecra_root """ + str(OciAutomation.ecra_root) + """ --exacloud_root """ + str(OciAutomation.exacloud_root) +"""
            
            """
            adding_cabinet = subprocess.Popen(["ssh", "-i", "./dbaas_sshkey.priv", "%s" % self.ecra_host, COMMAND],
                                         shell=False,
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE)
    
            adding_cabinet.wait()
            result = adding_cabinet.stdout.readlines()
            if not result:
                error = adding_cabinet.stderr.readlines()
                print >>sys.stderr, "ERROR: %s" % error
                sys.exit()
            else:
                print result
    
        # composing a cluster
    def compose_cluster(self):
            while compose_count > 0:
                COMMAND = """
                        echo EXADATA_CLOUD_EXACLOUD_REST_USER='admin'
                        echo EXADATA_CLOUD_EXACLOUD_REST_PASSWORD='Welcome1!'
                        cd """+exacloud_root+'/vcn_cloud'+"""
                        ./cabinets_n_clusters_util.py -i """+ str(OciAutomation.flat_file) +""" -c -s 3cell2comp2ibsw2pdu1ethsw -m """+ str(cluster_series) +\
                """ -d SEA2 --ecra_root """+ str(OciAutomation.ecra_root) +""" --exacloud_root """+str(OciAutomation.exacloud_root)+"""
                
                """
                composing_cluster = subprocess.Popen(["ssh", "-i", "./dbaas_sshkey.priv", "%s" % self.ecra_host, COMMAND],
                                             shell=False,
                                             stdout=subprocess.PIPE,
                                             stderr=subprocess.PIPE)
    
                composing_cluster.wait()
                result = composing_cluster.stdout.readlines()
                if not result:
                    error = composing_cluster.stderr.readlines()
                    print >> sys.stderr, "ERROR: %s" % error
                    sys.exit()
                else:
                    print result
                compose_count-=1
    
    def create_service(self):
            # use the alias created before in the script,take alias name also as the script input
            # keeping the <alias_name> for cli as 'atpecli_new'
            COMMAND = """
                    alias atpecli_new="/"""+ self.dir_name +'/oracle/ecra_installs/'+ self.ecra_name +'/ecracli/ecracli -c ' \
                                     '/'+ self.dir_name +'/oracle/ecra_installs/'+ self.ecra_name +"""/ecracli/ecracli.cfg" >> ~/.bashrc 
            """
            setting_cli_alias = subprocess.Popen(["ssh", "-i", "./dbaas_sshkey.priv", "%s" % self.ecra_host, COMMAND],
                                         shell=False,
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE)
            result = setting_cli_alias.stdout.readlines()
            if not result:
                error = setting_cli_alias.stderr.readlines()
                print >> sys.stderr, "ERROR: %s" % error
                sys.exit()
            else:
                print result
    
            # creating service
            COMMAND = """
                    atpecli_new create_service env=gen2 gen2PayloadPath="""+str(OciAutomation.flat_file)+'/'+str(OciAutomation.payload_json_file)+"""
            """
            creating_service = subprocess.Popen(["ssh", "-i", "./dbaas_sshkey.priv", "%s" % self.ecra_host, COMMAND],
                                         shell=False,
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE)
    
            creating_service.wait()
            result = creating_service.stdout.readlines()
            if not result:
                error = creating_service.stderr.readlines()
                print >> sys.stderr, "ERROR: %s" % error
                sys.exit()
            else:
                print result
    
    def check_create_service_logs(self):
    
            #opening the thread log file for checking whether service creation completed successfully
            COMMAND = """
                    ls """+OciAutomation.exacloud_root+'log/threads/'+""" -t *vmgi_install* | head -n1 
            """
            create_service_logFile_fetch = subprocess.Popen(["ssh", "-i", "./dbaas_sshkey.priv", "%s" % self.ecra_host, COMMAND],
                                         shell=False,
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE)
    
            create_service_logFile_fetch.wait()
            log_file = create_service_logFile_fetch.stdout.readlines()
            if not result:
                error = create_service_logFile_fetch.stderr.readlines()
                print >> sys.stderr, "ERROR: %s" % error
                sys.exit()
            else:
                print result
    
            log_file_path = exacloud_root + '/log/threads/' + log_file
            p = multiprocessing.Process(target = install_completed, args= (log_file_path,'Create Service completed'))
            p.start()
    
            #wait for service creation process for 2 hrs(7200 seconds)
            p.join(7200)
    
            killIfAlive(p)
    
            print "Create service completed successfully!"
    
    def create_starter_db(self):
    
            #create the starter db,pass the cluster_name as input
            COMMAND = """
                    sudo su oracle
                    atpecli_new create_starter """+self.cluster_name+""" dbVersion=19.0.0.0
            """
            creating_starter_db = subprocess.Popen(["ssh", "-i", "./dbaas_sshkey.priv", "%s" % self.ecra_host, COMMAND],
                                         shell=False,
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE)
    
            creating_starter_db.wait()
            result = creating_starter_db.stdout.readlines()
            if not result:
                error = creating_starter_db.stderr.readlines()
                print >> sys.stderr, "ERROR: %s" % error
                sys.exit()
            else:
                print result
            print "Starter DB created successfully!"
    
        #POD creation in DomU
    def pod_creation(self):
            pod_creation_host = "opc@129.213.229.158"
            COMMAND="""
                     curl -u ravindranath.chennoju@oracle.com:'DdxA2#tz6IA:}V]xjE(W' -X GET -O https://swiftobjectstorage.us-phoenix-1.oraclecloud.com/v1/intdbaasecra/LargeFilesDisposableAfterUse/swagger-java-client.zip
                     unzip swagger-java-client.zip
                     cd swagger-java-client/src/test/java/
                     export HOST_IP='http://10.0.20.177:7070'
            """
            #Creating 3 pods
            for i in range(3):
               COMMAND += """
                             export POD_NAME='POD'"""+str(i+1)+"""
                             javac -cp "../../../target/lib/*:../../../target/*" io/swagger/client/api/CreateDatabaseTestBasic.java
                             java -cp ".:../../../target/lib/*:../../../target/*" org.junit.runner.JUnitCore io.swagger.client.api.CreateDatabaseTestBasic
               """
    
            creating_pods = subprocess.Popen(["ssh","-i","./dbaas_sshkey.priv", "%s" % pod_creation_host, COMMAND],
                                   shell=False,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            result = creating_pods.stdout.readlines()
            if not result:
                error = creating_pods.stderr.readlines()
                print >>sys.stderr, "ERROR: %s" % error
            else:
                print result
    
    
    def run(self):
    
            parameter_calculation()
            fetch_flatfile_payload_json_details()
            download_tarfile()
            install_ecra()
            check_ecra_installation_logs()
            add_cabinet()
            compose_cluster()
            create_service()
            check_create_service_logs()
            create_starter_db()
            pod_creation()
    
    if __name__ == '__main__':
        OciAutomation obj1
        run()
    
    
    
    
    
    
    
    
    
    
    
    