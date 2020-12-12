def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
# Loop that will add any additional arguments, (key, value pairs) to the empty profile dicitonary.  
    for key, value in user_info.items():
        profile[key] = value
    return profile

# Calling the build_profile function and passing arguments
user_profile = build_profile('albert', 'einstein', 
                              location = 'princeton',
                              field = 'physics')
print(user_profile)
                                            