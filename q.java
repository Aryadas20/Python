void editContact() {
    boolean search = false;

    System.out.print("\nEnter First Name: ");
    String firstName = scanner.next();

    for (Contacts contact : list){

        if (firstName.equals(contact.getFirstName())){
            System.out.println("Contact Found");
            System.out.println("Edit Contact Details....");

            System.out.print("Enter First Name: ");
            contact.setFirstName(scanner.nextLine());

            System.out.print("Enter Last Name: ");
            contact.setLastName(scanner.nextLine());

            System.out.print("Enter Address:  ");
            contact.setAddress(scanner.nextLine());

            System.out.print("Enter City: ");
            contact.setCity(scanner.nextLine());

            System.out.print("Enter State: ");
            contact.setState(scanner.nextLine());

            System.out.print("Enter Zip-code: ");
            contact.setZip(scanner.nextLine());

            System.out.print("Enter Phone Number: ");
            contact.setPhoneNumber(scanner.nextLine());

            System.out.print("Enter Email-ID: ");
            contact.setEmail(scanner.nextLine());
            break;
        }
        else
            System.out.println("Contact Not Found");
    }

