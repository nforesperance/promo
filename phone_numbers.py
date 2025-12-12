import phonenumbers as pn
from phonenumbers import geocoder, carrier

def get_phone_info(phone_number):
    """
    Get the geographical location and carrier of a phone number.
    
    Args:
        phone_number (str): The phone number in E.164 format.
        
    Returns:
        dict: A dictionary containing the location and carrier of the phone number.
    """
    try:
        # Parse the phone number string into a PhoneNumber object
        parsed_number = pn.parse(phone_number, None)
        
        is_valid = pn.is_valid_number(parsed_number)
        if not is_valid:
            return {"error": "Invalid phone number"}
        dial_code = parsed_number.country_code
        print(f"Parsed Number: {parsed_number}")
        print(f"Is Valid: {is_valid}")
        print(f"Dial Code: {dial_code}")
        country_code = pn.region_code_for_number(parsed_number)
        print(f"Country Code: {country_code}")
        

        region_name = pn.region_code_for_country_code(dial_code)
        print(f"Region Name: {region_name}")
        
        formatted_number = pn.format_number(parsed_number, pn.PhoneNumberFormat.INTERNATIONAL)
        print(f"Formatted Number: {formatted_number}")
        
        # Get the geographical location
        location = geocoder.description_for_number(parsed_number, "en")
        country = geocoder.country_name_for_number(parsed_number, "en")
        
        
        # Get the carrier information
        service_provider = carrier.name_for_number(parsed_number, "en")
        
        return {
            "location": location,
            "carrier": service_provider,
            "country": country,
        }
    except Exception as e:
        return {"error": str(e)}
# Example usage
if __name__ == "__main__":
    phone_number = "+237694104664"  # Example phone number in E.164 format
    info = get_phone_info(phone_number)
    print(info)