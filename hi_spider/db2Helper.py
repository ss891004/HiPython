
#-*-coding-*-
import ibm_db

conn= None;

try:
    conn = ibm_db.connect("DATABASE=mydb;HOSTNAME=32.13.23.243;PORT=50001;PROTOCOL=TCPIP;UID=db2inst1;PWD=654321;", "", "");

    if conn:
        sql = "SELECT * FROM DB2INST1.T_TEST";
        stmt = ibm_db.exec_immediate(conn, sql);
        result = ibm_db.fetch_both(stmt);


        while( result ):
            print ("员工编号 :", result[0], result[1])
            print ('-----------------')
            result = ibm_db.fetch_both(stmt)

except Exception as ex:
    print(ex)

finally:
    ibm_db.free_stmt(stmt);
    ibm_db.close(conn); 
