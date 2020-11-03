a =[{
                                        "actionCodes": "",
                                        "calculationExpression": "",
                                        "calculationType": "Raw",
                                        "dataCollectionItemName": "Item%s"%(2001+i),
                                        "dataCollectionMode": "Manual",
                                        "dataCollectionUnit": "",
                                        "dataType": "Float",
                                        "dataValue":  "${__P(dataValue_B)}",
                                        "historyRequiredFlag": "true",
                                        "itemType": "Raw",
                                        "measurementType": "Control Job",
                                        "sitePosition": "",
                                        "specCheckResult": "",
                                        "targetValue": "10.0",
                                        "waferID": "null",
                                        "waferPosition": ""
                                    } for i in range(2000)]
print(a)