contacts
========

This project is to create a command line based program that will aid the user in the handling of contacts and contact information for those contacts. The user will be able to sort their contacts by groups for more convienient organization and to make it easier to find the person they are trying to contact. The contacts will be kept in a list of all contacts and inidivual lists for each group.

To run the program:
	./manager.py <contacts.yaml>
where contacts.yaml is am existing contact book. One has been provided and is called 'contacts.yaml'. Type 'help' to get list of commands.

Due to time constraints, changes made to contacts in the program cannot not be saved. Also, we did not have time to implement strict error checking for all command syntax, so some sytax errors may cause the program to crash.

<!-- more -->

The project will use parts of the Unix design philosiphy in its implementation. It will use orthogonality in that we are keeping the data handling portions of the code as seperate as possible from the parts of the code taht the user will interface with. We are also using the silence is golden aspect in that the part parts of the code that communicat with each other only share the information neccessary for the other part to complete its objective. 
