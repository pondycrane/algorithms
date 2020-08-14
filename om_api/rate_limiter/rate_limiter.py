"""
Problem: Design rate limiter — A rate limiter is a tool that
monitors the number of requests per a window time a service 
agrees to allow. If the request count exceeds the number agreed 
by the service owner and the user (in a decided window time), 
the rate limiter blocks all the excess calls(say by throwing 
exceptions). The user can be a human or any other service
(ex: in a micro service based architecture)

Example: A device with a specific ip address can only make 
10 ticket bookings per minute to a show booking website. 
Or a service A can hit service B with a rate of at most 
500 req/sec. All the excess requests get rejected.
"""
