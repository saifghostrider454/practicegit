{
    "metadata": {
        "kernelspec": {
            "name": "SQL",
            "display_name": "SQL",
            "language": "sql"
        },
        "language_info": {
            "name": "sql",
            "version": ""
        }
    },
    "nbformat_minor": 2,
    "nbformat": 4,
    "cells": [
        {
            "cell_type": "code",
            "source": [
                "CREATE TABLE EmployeeDemographics (\r\n",
                "EmployeeID int,\r\n",
                "FirstaName varchar(50),\r\n",
                "LastName varchar(50),\r\n",
                "Age int,\r\n",
                "Gender varchar(50)\r\n",
                ")"
            ],
            "metadata": {
                "azdata_cell_guid": "ab2951f0-f87a-49ba-b789-1300f02c08ef",
                "language": "sql"
            },
            "outputs": [
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "Commands completed successfully."
                    },
                    "metadata": {}
                },
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "Total execution time: 00:00:00.012"
                    },
                    "metadata": {}
                }
            ],
            "execution_count": 1
        },
        {
            "cell_type": "code",
            "source": [
                "CREATE TABLE EmployeeSalary (\r\n",
                "EmployeeID int,\r\n",
                "JobTitle varchar(50),\r\n",
                "Salary int\r\n",
                ")"
            ],
            "metadata": {
                "language": "sql",
                "azdata_cell_guid": "f4a88e01-5a4f-4328-8fff-b00bf5c0758f"
            },
            "outputs": [
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "Commands completed successfully."
                    },
                    "metadata": {}
                },
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "Total execution time: 00:00:00.002"
                    },
                    "metadata": {}
                }
            ],
            "execution_count": 2
        },
        {
            "cell_type": "code",
            "source": [
                "Insert into EmployeeDemographics VALUES\r\n",
                "(1001, 'Jim', 'Halpert', 30, 'Male'),\r\n",
                "(1002, 'Pam', 'Beasley', 30, 'Female'),\r\n",
                "(1003, 'Dwight', 'Schrute', 29, 'Male'),\r\n",
                "(1004, 'Angela', 'Martin', 31, 'Female'),\r\n",
                "(1005, 'Toby', 'Flenderson', 32, 'Male'),\r\n",
                "(1006, 'Michael', 'Scott', 35, 'Male'),\r\n",
                "(1007, 'Meredith', 'Palmer', 32, 'Female'),\r\n",
                "(1008, 'Stanley', 'Hudson', 38, 'Male'),\r\n",
                "(1009, 'Kevin', 'Malone', 31, 'Male')"
            ],
            "metadata": {
                "language": "sql",
                "azdata_cell_guid": "54909b49-affc-47a6-8ddb-46340b0d1129"
            },
            "outputs": [
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "(9 rows affected)"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "Total execution time: 00:00:00.004"
                    },
                    "metadata": {}
                }
            ],
            "execution_count": 3
        },
        {
            "cell_type": "code",
            "source": [
                "Insert Into EmployeeSalary VALUES\r\n",
                "(1001, 'Salesman', 45000),\r\n",
                "(1002, 'Receptionist', 36000),\r\n",
                "(1003, 'Salesman', 63000),\r\n",
                "(1004, 'Accountant', 47000),\r\n",
                "(1005, 'HR', 50000),\r\n",
                "(1006, 'Regional Manager', 65000),\r\n",
                "(1007, 'Supplier Relations', 41000),\r\n",
                "(1008, 'Salesman', 48000),\r\n",
                "(1009, 'Accountant', 42000)"
            ],
            "metadata": {
                "language": "sql",
                "azdata_cell_guid": "24bf6bf5-1015-499b-8627-6f422355e6b5"
            },
            "outputs": [
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "(9 rows affected)"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "Total execution time: 00:00:00.002"
                    },
                    "metadata": {}
                }
            ],
            "execution_count": 4
        },
        {
            "cell_type": "code",
            "source": [
                "SELECT *\r\n",
                "FROM SQLTutorial.dbo.EmployeeSalary"
            ],
            "metadata": {
                "language": "sql",
                "azdata_cell_guid": "947a5f11-15b2-4712-83ad-a27877de0f05",
                "tags": []
            },
            "outputs": [
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "(9 rows affected)"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "Total execution time: 00:00:00.056"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "execute_result",
                    "metadata": {},
                    "execution_count": 5,
                    "data": {
                        "application/vnd.dataresource+json": {
                            "schema": {
                                "fields": [
                                    {
                                        "name": "EmployeeID"
                                    },
                                    {
                                        "name": "JobTitle"
                                    },
                                    {
                                        "name": "Salary"
                                    }
                                ]
                            },
                            "data": [
                                {
                                    "EmployeeID": "1001",
                                    "JobTitle": "Salesman",
                                    "Salary": "45000"
                                },
                                {
                                    "EmployeeID": "1002",
                                    "JobTitle": "Receptionist",
                                    "Salary": "36000"
                                },
                                {
                                    "EmployeeID": "1003",
                                    "JobTitle": "Salesman",
                                    "Salary": "63000"
                                },
                                {
                                    "EmployeeID": "1004",
                                    "JobTitle": "Accountant",
                                    "Salary": "47000"
                                },
                                {
                                    "EmployeeID": "1005",
                                    "JobTitle": "HR",
                                    "Salary": "50000"
                                },
                                {
                                    "EmployeeID": "1006",
                                    "JobTitle": "Regional Manager",
                                    "Salary": "65000"
                                },
                                {
                                    "EmployeeID": "1007",
                                    "JobTitle": "Supplier Relations",
                                    "Salary": "41000"
                                },
                                {
                                    "EmployeeID": "1008",
                                    "JobTitle": "Salesman",
                                    "Salary": "48000"
                                },
                                {
                                    "EmployeeID": "1009",
                                    "JobTitle": "Accountant",
                                    "Salary": "42000"
                                }
                            ]
                        },
                        "text/html": [
                            "<table>",
                            "<tr><th>EmployeeID</th><th>JobTitle</th><th>Salary</th></tr>",
                            "<tr><td>1001</td><td>Salesman</td><td>45000</td></tr>",
                            "<tr><td>1002</td><td>Receptionist</td><td>36000</td></tr>",
                            "<tr><td>1003</td><td>Salesman</td><td>63000</td></tr>",
                            "<tr><td>1004</td><td>Accountant</td><td>47000</td></tr>",
                            "<tr><td>1005</td><td>HR</td><td>50000</td></tr>",
                            "<tr><td>1006</td><td>Regional Manager</td><td>65000</td></tr>",
                            "<tr><td>1007</td><td>Supplier Relations</td><td>41000</td></tr>",
                            "<tr><td>1008</td><td>Salesman</td><td>48000</td></tr>",
                            "<tr><td>1009</td><td>Accountant</td><td>42000</td></tr>",
                            "</table>"
                        ]
                    }
                }
            ],
            "execution_count": 5
        },
        {
            "cell_type": "code",
            "source": [
                "SELECT *\r\n",
                "FROM EmployeeDemographics \r\n",
                "WHERE Age BETWEEN 21 AND 30"
            ],
            "metadata": {
                "language": "sql",
                "azdata_cell_guid": "eea18c23-9e65-48a3-8cad-d08e088cf1fb"
            },
            "outputs": [
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "(3 rows affected)"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "Total execution time: 00:00:00.011"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "execute_result",
                    "metadata": {},
                    "execution_count": 6,
                    "data": {
                        "application/vnd.dataresource+json": {
                            "schema": {
                                "fields": [
                                    {
                                        "name": "EmployeeID"
                                    },
                                    {
                                        "name": "FirstaName"
                                    },
                                    {
                                        "name": "LastName"
                                    },
                                    {
                                        "name": "Age"
                                    },
                                    {
                                        "name": "Gender"
                                    }
                                ]
                            },
                            "data": [
                                {
                                    "EmployeeID": "1001",
                                    "FirstaName": "Jim",
                                    "LastName": "Halpert",
                                    "Age": "30",
                                    "Gender": "Male"
                                },
                                {
                                    "EmployeeID": "1002",
                                    "FirstaName": "Pam",
                                    "LastName": "Beasley",
                                    "Age": "30",
                                    "Gender": "Female"
                                },
                                {
                                    "EmployeeID": "1003",
                                    "FirstaName": "Dwight",
                                    "LastName": "Schrute",
                                    "Age": "29",
                                    "Gender": "Male"
                                }
                            ]
                        },
                        "text/html": [
                            "<table>",
                            "<tr><th>EmployeeID</th><th>FirstaName</th><th>LastName</th><th>Age</th><th>Gender</th></tr>",
                            "<tr><td>1001</td><td>Jim</td><td>Halpert</td><td>30</td><td>Male</td></tr>",
                            "<tr><td>1002</td><td>Pam</td><td>Beasley</td><td>30</td><td>Female</td></tr>",
                            "<tr><td>1003</td><td>Dwight</td><td>Schrute</td><td>29</td><td>Male</td></tr>",
                            "</table>"
                        ]
                    }
                }
            ],
            "execution_count": 6
        },
        {
            "cell_type": "code",
            "source": [
                "SELECT EmployeeID, Salary \r\n",
                "FROM EmployeeSalary\r\n",
                "WHERE Salary > (SELECT AVG(Salary) FROM EmployeeSalary)"
            ],
            "metadata": {
                "language": "sql",
                "azdata_cell_guid": "2c273a39-4a12-49c7-96bb-3b7d5643825d",
                "tags": []
            },
            "outputs": [
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "(3 rows affected)"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "Total execution time: 00:00:00.009"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "execute_result",
                    "metadata": {},
                    "execution_count": 9,
                    "data": {
                        "application/vnd.dataresource+json": {
                            "schema": {
                                "fields": [
                                    {
                                        "name": "EmployeeID"
                                    },
                                    {
                                        "name": "Salary"
                                    }
                                ]
                            },
                            "data": [
                                {
                                    "EmployeeID": "1003",
                                    "Salary": "63000"
                                },
                                {
                                    "EmployeeID": "1005",
                                    "Salary": "50000"
                                },
                                {
                                    "EmployeeID": "1006",
                                    "Salary": "65000"
                                }
                            ]
                        },
                        "text/html": [
                            "<table>",
                            "<tr><th>EmployeeID</th><th>Salary</th></tr>",
                            "<tr><td>1003</td><td>63000</td></tr>",
                            "<tr><td>1005</td><td>50000</td></tr>",
                            "<tr><td>1006</td><td>65000</td></tr>",
                            "</table>"
                        ]
                    }
                }
            ],
            "execution_count": 9
        },
        {
            "cell_type": "code",
            "source": [
                "SELECT Gender, COUNT(EmployeeID) as Total\r\n",
                "FROM EmployeeDemographics\r\n",
                "GROUP BY Gender"
            ],
            "metadata": {
                "language": "sql",
                "azdata_cell_guid": "e0a7c399-6714-4971-a364-a5971ca30e02"
            },
            "outputs": [
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "(2 rows affected)"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "Total execution time: 00:00:00.010"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "execute_result",
                    "metadata": {},
                    "execution_count": 14,
                    "data": {
                        "application/vnd.dataresource+json": {
                            "schema": {
                                "fields": [
                                    {
                                        "name": "Gender"
                                    },
                                    {
                                        "name": "Total"
                                    }
                                ]
                            },
                            "data": [
                                {
                                    "Gender": "Female",
                                    "Total": "3"
                                },
                                {
                                    "Gender": "Male",
                                    "Total": "6"
                                }
                            ]
                        },
                        "text/html": [
                            "<table>",
                            "<tr><th>Gender</th><th>Total</th></tr>",
                            "<tr><td>Female</td><td>3</td></tr>",
                            "<tr><td>Male</td><td>6</td></tr>",
                            "</table>"
                        ]
                    }
                }
            ],
            "execution_count": 14
        },
        {
            "cell_type": "code",
            "source": [
                ""
            ],
            "metadata": {
                "language": "sql",
                "azdata_cell_guid": "0982b3b9-5716-4ddb-9e8d-b144e36e5181"
            },
            "outputs": [],
            "execution_count": null
        },
        {
            "cell_type": "code",
            "source": [
                ""
            ],
            "metadata": {
                "language": "sql",
                "azdata_cell_guid": "34c2ed72-ac60-4a56-8103-88fa68916f38"
            },
            "outputs": [],
            "execution_count": null
        },
        {
            "cell_type": "code",
            "source": [
                ""
            ],
            "metadata": {
                "language": "sql",
                "azdata_cell_guid": "0313a718-e27b-4692-84d8-0cfb7861a03a"
            },
            "outputs": [],
            "execution_count": null
        },
        {
            "cell_type": "code",
            "source": [
                ""
            ],
            "metadata": {
                "language": "sql",
                "azdata_cell_guid": "d37c5d12-16de-453b-a4cf-1d4f55bbc8c5"
            },
            "outputs": [],
            "execution_count": null
        },
        {
            "cell_type": "code",
            "source": [
                ""
            ],
            "metadata": {
                "language": "sql",
                "azdata_cell_guid": "6cf1695d-2ec1-4416-af16-d0cb582dd9c6"
            },
            "outputs": [],
            "execution_count": null
        }
    ]
}