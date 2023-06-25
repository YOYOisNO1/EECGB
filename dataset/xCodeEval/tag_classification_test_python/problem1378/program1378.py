    import math
    ppl, teams = [int(i) for i in input().split()]
    
# def cnt(z):
    # 	return int((int(z/2))*(z-1))
    
def cnt(z):
    	# return int((n * (n-1))/2)
    	# return int((n/2)*(n-1))
    	return int(z*(z-1)//2)
    
    if teams == 1:
    	print(cnt(ppl), cnt(ppl))
    else:
    	# equal = math.ceil(ppl/teams)
    	# mn = cnt(equal) * teams
    	# last_team = equal*teams - ppl
    	# # print(mn, last_team)
    	# if last_team !=0:
    	# 	mn-= cnt(equal)
    	# 	mn+=cnt(last_team)
    
    	equal = math.floor(ppl/teams)
    	large_teams = ppl%teams
    	mn = cnt(equal+1) * large_teams + cnt(equal) * (teams - large_teams)
    
    	print(mn, cnt(ppl-teams+1))