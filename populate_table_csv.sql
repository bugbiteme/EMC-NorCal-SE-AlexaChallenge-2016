.mode csv
.import /Users/levyl1/Projects/EMC-NorCal-SE-AlexaChallenge-2016/DSH.csv tbl_installbase

select CS_CUSTOMER_NAME, PRODUCT_GROUP, ITEM_SERIAL_NUMBER 
	from tbl_installbase 
	where PRODUCT_GROUP='VNX5800' or PRODUCT_GROUP='VNX5300';
