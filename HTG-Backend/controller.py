from model import *
def controller(model):
    # Populate model.rooms with data as needed
    # Prompt for patient information
    # Example: patient_info = {"name": "John Doe", "age": 30, "infectious": True}
    patient_info = get_patient_information()  # Get patient information
    patient = model.new_patient(**patient_info)
    # Additional logic to manage patients

def input_yes_no(prompt):
    """Utility function for yes/no inputs."""
    while True:
        answer = input(prompt + " (yes/no): ").strip().lower()
        if answer in ['yes', 'no']:
            return answer == 'yes'
        print("Please answer with 'yes' or 'no'.")

def input_choice(prompt, choices):
    """Utility function for choosing from provided options."""
    choice_str = "/".join(choices)
    while True:
        answer = input(f"{prompt} ({choice_str}): ").strip().lower()
        if answer in choices:
            return answer
        print(f"Please choose from {choice_str}.")

def get_patient_information():
    patient_info = {}

    # Patient name
    patient_info['name'] = input("Patient Name: ").strip()

    # Patient gender
    patient_info['gender'] = input_choice("Patient Gender", ['male', 'female', 'other'])

    # Patient age and shared room eligibility
    while True:
        try:
            patient_info['age'] = int(input("Patient Age: ").strip())
            if patient_info['age'] < 0:
                print("Age cannot be negative. Please enter a valid age.")
            else:
                break
        except ValueError:
            print("Please enter a valid number for age.")

    # Isolation for contagious reasons
    patient_info['isolation_contagious'] = input_yes_no("Isolation Required (contagious)")

    # Isolation for palliative care
    patient_info['isolation_palliative_care'] = input_yes_no("Isolation Required (palliative care)")

    # Enhanced observation required
    patient_info['enhanced_observation_required'] = input_yes_no("Enhanced observation is required")

    # Enhanced supervision required
    patient_info['enhanced_supervision_required'] = input_yes_no("Enhanced supervision is required")

    # Apply logic based on input, e.g., setting room requirements
    # This part depends on how your model handles these flags, so adjust accordingly.
    # Example:
    patient_info['requires_single_room'] = patient_info.get('enhanced_supervision_required') or \
                                           patient_info.get('isolation_contagious') or \
                                           patient_info.get('enhanced_observation_required') or \
                                           (patient_info['age'] < 18)

    # Print or return the collected information for further processing
    return patient_info