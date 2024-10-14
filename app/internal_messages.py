"""
Defines the messages used within the app context.
"""

# Messages for logger

logger_message_starting_messenger = '>>> STARTING COLUMBA MESSENGER'
logger_message_searching_events = 'Searching events at {time}'
logger_message_launching_event = '--- Launching event: {event_id}'

# Messages for API responses

response_message_successful = 'Successful {method}.'
response_message_undefined_error = 'Undefined error.'

response_message_bad_request_body = 'Request body type is incorrect.'
response_message_hard_unexpected_error = 'An unexpected error occured:\n{full_traceback}'
response_message_invalid_categorical_value = 'Invalid categorical value ({invalid_value}). Valid values are: {categorical_values}.'
response_message_invalid_field_names = 'There are invalid field names ({invalid_names}). The valid names are: {valid_names}.'
response_message_invalid_field_type = "The field type must be '{valid_type}', not '{invalid_type}'."
response_message_invalid_elements_type = "The type of all the elements must be '{valid_type}."
response_message_invalid_email_addresses = "There are invalid email addresses."
response_message_invalid_period_format = "Period format must be: 'Ad Bh Cm', where A, B, C are days, hours and minutes, respectively."
response_message_invalid_query_params = 'Invalid query parameters ({invalid_names}). Valid parameters are: {valid_names}.'
response_message_invalid_runtime_format = 'Runtime format must be: YYYY-MM-DD hh:mm'
response_message_missing_required_fields = 'Some mandatory fields are missing ({missing_required_fields}).'
response_message_no_request_body = 'Request body is missing.'
response_message_not_found = 'The requested event was not found.'
response_message_soft_unexpected_error = 'An unexpected error occured.'

base_field_error_message = "Errors in field '{field_name}':"

# Messages for internal bugs

admin_message_missing_env_vars = 'THE FOLLOWING ENV VARIABLES ARE MISSING: {env_vars}.'
admin_message_not_jsonifyable_response = 'THE APPLICATION CAN ONLY RESPOND WITH OBJECTS THAT CAN BE CONVERTED TO JSON FORMAT.'
admin_message_not_pythonifyable_request = "JSON REQUEST BODY CANNOT BE CONVERTED TO TYPE '{type}'."
admin_message_unmanaged_case = "THE CASE '{case}' MUST BE CATCHED (IF INVALID) OR INCLUDED (IF VALID) BEFORE REACHING THIS POINT."