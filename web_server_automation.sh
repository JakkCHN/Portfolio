#!/bin/bash

# Function to display menu
display_menu() {
    echo "Web Server Automation Script"
    echo "1. Check Directory Structure"
    echo "2. List Files in a Directory"
    echo "3. Read/Write to a File"
    echo "4. Send Email"
    echo "5. Get User Input"
    echo "6. Exit"
}

# Function to check if a directory exists
check_directory_exists() {
    local directory_path=$1

    if [ -d "$directory_path" ]; then
        echo "Directory $directory_path exists."
        return 0
    else
        echo "Directory $directory_path does not exist."
        return 1
    fi
}

# Function to list files in a directory
list_files() {
    read -p "Enter the directory path: " directory_path

    if check_directory_exists "$directory_path"; then
        echo "Listing files in $directory_path:"
        ls "$directory_path"
    fi
}

# Function to read/write to a file
read_write_file() {
    read -p "Enter the file path: " file_path

    if [ -f "$file_path" ]; then
        echo "1. Read File"
        echo "2. Write to File"
        read -p "Enter your choice: " choice

        case $choice in
            1)
                echo "Reading contents of $file_path:"
                cat "$file_path"
                ;;
            2)
                read -p "Enter text to write to $file_path: " content
                echo "$content" >> "$file_path"
                echo "Content written to $file_path"
                ;;
            *)
                echo "Invalid choice"
                ;;
        esac
    else
        echo "File not found: $file_path"
    fi
}

# Function to send email
send_email() {
    read -p "Enter recipient email address: " recipient_email
    read -p "Enter subject: " subject
    read -p "Enter email body: " body

    echo "Sending email to $recipient_email..."
    # Add your email sending logic here
    echo "Email sent successfully."
}

# Function to get user input
get_user_input() {
    read -p "Enter user input: " user_input
    echo "User input: $user_input"
}

# Main script
while true; do
    display_menu

    read -p "Enter your choice (1-6): " choice

    case $choice in
        1)
            check_directory_structure
            ;;
        2)
            list_files
            ;;
        3)
            read_write_file
            ;;
        4)
            send_email
            ;;
        5)
            get_user_input
            ;;
        6)
            echo "Exiting script. Goodbye!"
            exit 0
            ;;
        *)
            echo "Invalid choice. Please enter a number between 1 and 6."
            ;;
    esac
done

