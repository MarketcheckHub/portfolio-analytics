CONFIG = {
    # need analysis for this client, based on vin, sale date and mileage
    # we need to check when the vin came to our inventory for the first time
    # we need to find the mcp of the vin and compare it with the listing price on the first day
    'adesa': {
        'api_key': 'adesa_api_key',
        'file_path': 'adesa/adesa.csv',
    }
}
