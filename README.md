#### **Sari-sari Store App**

A program depicting the everyday Tindahan of Filipinos.

User will enter through the http://127.0.0.1:8000/home/, and here
he can see all the current Paninda of the Sari-sari Store.

He can click through the "TINGNAN" button on each paninda
to see its details.
Ex: http://127.0.0.1:8000/home/1/

He can order that item through the Order "Item" button:
http://127.0.0.1:8000/issue_item/1/

	Here, he is required to input the quantity, the amount he
	will pay, and his name.

	Once he clicked the Confirm button, he will be shown 
	all the receipts made by the tindahan. http://127.0.0.1:8000/receipt/

	Clicking on the "Final Receipt" button on each receipt, he
	will be directed to the order summary for that transaction.
	http://127.0.0.1:8000/receipt/1/

He can click the Update "Item" to modify the name, price, and increase the
quantity of that paninda.
http://127.0.0.1:8000/update_stock/1/

On the other hand, he can click the Delete "Item" to completely delete
that paninda, and he will be redirected to /home/

User can also Add New Item, for this he will be required to supply the name,
price, and quantity for that new paninda.
http://127.0.0.1:8000/add_new_stock/

User can also view all the sales made by the Tindahan by navigating to:
http://127.0.0.1:8000/all_sales/

Note: Please install the modules inside requirements.txt"# sarisaristore_enriquez" 
