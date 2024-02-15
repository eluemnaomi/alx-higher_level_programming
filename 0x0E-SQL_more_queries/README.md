0X0E MySQL MORE QUERIES
Creating New MySQL User
CREATE USER statement is used

mysql> CREATE USER 'username'@'host' IDENTIFIED WITH 'authentication_plugin' BY 'password';

There are several options when it comes to choosing the user's authentication plugin;

auth_socket:
It provides strong security without requiring valid users to enter a password to access the database, but is also prevents remote connections, which can complicate things when external programs need to interact with MySQL.
caching_sha2_password
As an alternative the WITH 'authentication_plugin' portion of the syntax can be left entirely to have the user authenticate with MySQL's default plugin i.e 'caching_sha2_password'
mysql_native_password
This authentication is used in some versions of PHP that causes problems with 'caching_sha2_password'.
This plugin is older thought still secure.
Granting user permissioins
The general syntax is;

mysql> GRANT 'PRIVILEGE' ON database.table TO 'username'@'host';

The 'privilege' value defines what actions the user is allowed to perform on the specified 'database' and 'table'
Multiple privileges can be granted to the same user in one command by separating each with a comma
To illustrate, the following command grants a user global privileges to CREATE, ALTER, and DROP databases, tables, and users, as well as the power to INSERT, UPDATE, and DELETE data from any table on the server. It also grants the user the ability to query data with SELECT, create foreign keys with the REFERENCES keyword, and perform FLUSH operations with the RELOAD privilege.
GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD on . TO 'sammy'@'localhost' WITH GRANT OPTION;

To revoke a permission; REVOKE 'type_of_permission' ON database_name.table_name FROM 'username'@'host';
