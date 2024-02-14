import pandas as pd

# Reading the data
data = pd.ExcelFile("KPMG1.xlsx")

# Reading each file separately 
Transactions = pd.read_excel(data, 'Transactions')
NewCustomerList = pd.read_excel(data, 'NewCustomerList')
CustomerDemographic = pd.read_excel(data, 'CustomerDemographic')
CustomerAddress = pd.read_excel(data, 'CustomerAddress')

# Exploring Transactions Data Set
Transactions.head(5)

Transactions.info()

# Using only the required columns 
Transactions = Transactions.iloc[:, 0:13]
Transactions.head()

Transactions.info()

# Checking the shape of the data
Transactions.shape

# Checking for null values
Transactions.isnull().sum()

# Checking for duplicate values
Transactions.duplicated().sum()

# Check for uniqueness of each column
Transactions.nunique() 

# Exploring the columns
Transactions.columns

Transactions['order_status'].value_counts()

Transactions['brand'].value_counts()

Transactions['product_line'].value_counts()

Transactions['product_class'].value_counts()

Transactions['product_size'].value_counts()

Transactions['product_first_sold_date']

# Convert date column from integer to datetime
Transactions['product_first_sold_date'] = pd.to_datetime(Transactions['product_first_sold_date'], unit='s')
Transactions['product_first_sold_date'].head()

Transactions['product_first_sold_date'].head(20)

# Exploring New Customer List Data Set
NewCustomerList.head(5)

NewCustomerList.info()

# Dropping the unnamed columns
NewCustomerList.drop(['Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18',
       'Unnamed: 19', 'Unnamed: 20'], axis=1, inplace=True)

# Checking the shape of the dataset
NewCustomerList.shape

# Checking for null values
NewCustomerList.isnull().sum()

# Checking for duplicate values
NewCustomerList.duplicated().sum()

# Check for uniqueness of each column
NewCustomerList.nunique()

# Exploring the columns
NewCustomerList.columns

NewCustomerList['gender'].value_counts()

NewCustomerList[NewCustomerList.gender == "U"]

NewCustomerList['DOB'].value_counts()

NewCustomerList['job_industry_category'].value_counts()

NewCustomerList['wealth_segment'].value_counts()

NewCustomerList['state'].value_counts()

NewCustomerList['owns_car'].value_counts()

NewCustomerList['deceased_indicator'].value_counts()

# Exploring Customer Demographic Data Set
CustomerDemographic.head()

CustomerDemographic.info()

# Checking for null values
CustomerDemographic.isnull().sum()

# Checking for duplicate data
CustomerDemographic.duplicated().sum()

# Check for uniqueness of each column
CustomerDemographic.nunique()

# Exploring the columns
CustomerDemographic.columns

CustomerDemographic['gender'].value_counts()

# Re-naming the categories
CustomerDemographic['gender'] = CustomerDemographic['gender'].replace('F','Female').replace('M','Male').replace('Femal','Female').replace('U','Unspecified')

CustomerDemographic['gender'].value_counts()

CustomerDemographic['past_3_years_bike_related_purchases'].value_counts()

CustomerDemographic['DOB'].value_counts()

CustomerDemographic['job_title'].value_counts()

CustomerDemographic['job_industry_category'].value_counts()

CustomerDemographic['wealth_segment'].value_counts()

CustomerDemographic['deceased_indicator'].value_counts()

CustomerDemographic['owns_car'].value_counts()

CustomerDemographic['tenure'].value_counts()

# Exploring Customer Address Data Set
CustomerAddress.head(5)

CustomerAddress.info()

# Checking for null values.
CustomerAddress.isnull().sum()

# Checking for duplicate values
CustomerAddress.duplicated().sum()

# Check for uniqueness of each column
CustomerAddress.nunique()

# Exploring the columns
CustomerAddress['postcode'].value_counts()

CustomerAddress['state'].value_counts()

CustomerAddress['country'].value_counts()

CustomerAddress['property_valuation'].value_counts()