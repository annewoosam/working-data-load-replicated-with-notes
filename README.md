# working-data-load-replicated-with-notes

Describing process in readme.

These files illustrate the information needed to display data from a sql table to the web.

The data is seeded into database.sql and server.py interacts with model.py to route information requested by user inout
from the web (index.html) to the database as to what to display using routes that rely on ajax.js to help render the data using json.

Compared to the prior versions, most of the extra material has been stripped down.

That means though the relationships will need to be established when the pieces are merged.

To spin off additional displays, duplicate your last working folder.

Open the folder set in your code editor and proceding in an updward direction or downward direction open the files needed and edit the table name,
Model Name and field names as needed. 

You can globally change fields in most code editors but be careful. 

For example, if you globally change user you will need to check that you have not lower-cased the model name in model.py or server.py or you will have issues.

Also, there are some occasions, rare, but important that the plural is used rather than the singular. Changing user to suers or vice versa can cause issues. 

Generally, reference to table names are plural and everything else is singular.

When done, edit the database.sql file appropriately to create seed data. 

In this example, the seed data unlike json files or the comma separated tables of other examples, is tab separated and no quotation amrks are used.

When the seed data is complete, go to your terminal in the virtual environment and delete the old database and create a new one then populate it with the data you created to do this then load your server.

In our example, the file is using the table users.

So we use:

deletedb users
createdb users
psql users < database.sql

and troubleshoot any errors in database.sql if they arise.

then rehash deletedb, createdb and psql users till done.

Once there are no errors, you can psl users and use \dt and \d and then \q to dee teh tables, relationships, then quit.

After that you can run python3 server.py and launch your browser using localhost:5000.

Use the inspect element feature and terminal error codes to troubleshoot any additional issues. generally the top and last errors on the web page
will direct you where to start troubleshooting. You can also highlight the terms and error codes, right click and perform a web search.

To exit the Flask server use CTRL C if using a universal keyboard. Fix your files. Reload server.py, reload/empty your browser cache. 

Repeat as necessary then determine a process for merging the information.


