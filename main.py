from flywheel import Client
from typing import List, Optional


def test_basic_client_usage():
    """Test basic client initialization and usage"""
    client = Client(api_key="test_key")

    # Test client properties
    projects = client.projects
    groups = client.groups
    users = client.users
    jobs = client.jobs

    # Test finder methods
    all_projects = projects.find()
    first_project = projects.find_first()

    return client


def test_project_operations():
    """Test project-related operations"""
    client = Client(api_key="test_key")

    # Get a project
    project = client.get_project("project_id")

    # Access project properties
    project_id = project.id
    project_label = project.label
    project_description = project.description
    project_tags = project.tags
    project_info = project.info

    # Work with project subjects
    subjects = project.subjects
    all_subjects = subjects.find()

    # Add a subject
    new_subject = project.add_subject("subject_label")

    return project


def test_subject_operations():
    """Test subject-related operations"""
    client = Client(api_key="test_key")

    # Get a subject
    subject = client.get_subject("subject_id")

    # Access subject properties
    subject_id = subject.id
    subject_label = subject.label
    subject_code = subject.code
    subject_age = subject.age
    subject_sex = subject.sex

    # Work with subject sessions
    sessions = subject.sessions
    all_sessions = sessions.find()

    # Add a session
    new_session = subject.add_session("session_label")

    return subject


def test_session_operations():
    """Test session-related operations"""
    client = Client(api_key="test_key")

    # Get a session
    session = client.get_session("session_id")

    # Access session properties
    session_id = session.id
    session_label = session.label
    session_description = session.description
    session_timestamp = session.timestamp

    # Work with session acquisitions
    acquisitions = session.acquisitions
    all_acquisitions = acquisitions.find()

    # Add an acquisition
    new_acquisition = session.add_acquisition("acquisition_label")

    return session


def test_file_operations():
    """Test file-related operations"""
    client = Client(api_key="test_key")

    # Get a file
    file_entry = client.get_file("file_id")

    # Get project and access files
    project = client.get_project("project_id")
    project_files = project.files

    # Get a specific file
    specific_file = project.get_file("filename.txt")

    # Read file contents
    file_contents = project.read_file("filename.txt")

    return file_entry


def test_data_view_operations():
    """Test data view operations"""
    client = Client(api_key="test_key")

    # Create a data view
    data_view = client.View(
        columns=[
            {"src": "subject.label", "dst": "subject_label"},
            {"src": "session.label", "dst": "session_label"}
        ]
    )

    # Print available columns
    client.print_view_columns()

    # Execute view and get DataFrame
    df = client.read_view_dataframe(data_view, "container_id")

    # Execute view and get raw data
    raw_data = client.read_view_data(data_view, "container_id")

    return data_view


def test_finder_operations():
    """Test finder operations with different methods"""
    client = Client(api_key="test_key")

    # Test various finder methods
    projects = client.projects

    # Find all projects
    all_projects = projects.find()

    # Find first project
    first_project = projects.find_first()

    # Find one project (exact match)
    one_project = projects.find_one("label=MyProject")

    # Find with filters
    filtered_projects = projects.find("label=MyProject", sort="created:desc", limit=10)

    # Iterate over all projects
    for project in projects.iter():
        print(f"Project: {project.label}")
        break  # Just test the first one

    # Iterate with filter
    for project in projects.iter_find("label=MyProject"):
        print(f"Filtered project: {project.label}")
        break  # Just test the first one

    return projects


def test_gear_and_job_operations():
    """Test gear and job operations"""
    client = Client(api_key="test_key")

    # Get gear
    gear = client.get_gear("gear_id")

    # Get job
    job = client.get_job("job_id")

    # Retry job
    retry_result = client.retry_job("job_id")

    # Get all jobs
    all_jobs = client.jobs.find()

    return gear, job


def test_group_operations():
    """Test group operations"""
    client = Client(api_key="test_key")

    # Get all roles
    all_roles = client.get_all_roles()

    # Get group
    group = client.get_group("group_id")

    # Get all groups
    all_groups = client.groups.find()

    return group


def test_user_operations():
    """Test user operations"""
    client = Client(api_key="test_key")

    # Get current user
    current_user = client.get_current_user()

    # Get all users
    all_users = client.users.find()

    # Modify user
    client.modify_user("user_id", {"firstname": "John"})

    return current_user


def test_project_settings():
    """Test project settings operations"""
    client = Client(api_key="test_key")

    # Get project settings
    settings = client.get_project_settings("project_id")

    # Modify project settings
    client.modify_project_settings("project_id", {"viewer_apps": []})

    return settings


def test_view_operations():
    """Test view operations"""
    client = Client(api_key="test_key")

    # Get views
    views = client.get_views("view_id")

    # Add view
    view_result = client.add_view("container_id", {})

    # Delete view
    delete_result = client.delete_view("view_id")

    return views


def test_project_rules():
    """Test project rules operations"""
    client = Client(api_key="test_key")

    # Get project rules
    rules = client.get_project_rules("project_id")

    # Add project rule
    from flywheel import GearRuleInput
    rule_input = GearRuleInput()
    new_rule = client.add_project_rule("project_id", rule_input)

    # Remove project rule
    client.remove_project_rule("project_id", "rule_id")

    return rules


def test_error_handling():
    """Test error handling"""
    try:
        client = Client(api_key="invalid_key")
        project = client.get_project("nonexistent_project")
    except Exception as e:
        print(f"Expected error: {e}")


def main():
    """Main function to test all operations"""
    print("Testing basic client usage...")
    test_basic_client_usage()

    print("Testing project operations...")
    test_project_operations()

    print("Testing subject operations...")
    test_subject_operations()

    print("Testing session operations...")
    test_session_operations()

    print("Testing file operations...")
    test_file_operations()

    print("Testing data view operations...")
    test_data_view_operations()

    print("Testing finder operations...")
    test_finder_operations()

    print("Testing gear and job operations...")
    test_gear_and_job_operations()

    print("Testing group operations...")
    test_group_operations()

    print("Testing user operations...")
    test_user_operations()

    print("Testing project settings...")
    test_project_settings()

    print("Testing view operations...")
    test_view_operations()

    print("Testing project rules...")
    test_project_rules()

    print("Testing error handling...")
    test_error_handling()

    print("All tests completed!")


if __name__ == "__main__":
    main()
