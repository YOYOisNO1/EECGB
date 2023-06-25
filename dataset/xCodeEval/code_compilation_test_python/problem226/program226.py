def program226():
    total_price,rides,sprice,rupees = map(int,input().split())
    
    if(rupees / rides > sprice):
        print(sprice * total_rides)
    else:
        base_fare = (total_rides // ride) * rupees
        cement_fare = (total_rides % rides) * sprice
        print(base_fare + cement_fare)
    