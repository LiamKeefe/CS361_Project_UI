import json

stock = {
    "MSFT": 
        {
            "Company": "Microsoft Corp.",
            "Price" : 362.95,
            "Description": "Microsoft Corp. engages in the development and support of software, services, devices, and solutions. It operates through the following business segments: Productivity and Business Processes, Intelligent Cloud, and More Personal Computing."
            },
    "TSLA":
        {
            "Company": "Tesla Inc.",
            "Price" : 220.45,
            "Description" : "Tesla, Inc. engages in the design, development, manufacture, and sale of fully electric vehicles and energy generation and storage systems. "
                },
    "AMD" :
        {
           "Company" : "Advanced Micro Devices Inc.",
           "Price" : 113.58,
           "Description" : "Advanced Micro Devices, Inc. engages in the provision of semiconductor businesses. It operates through the following segments: Computing & Graphics, and Enterprise, Embedded and Semi-Custom."
        },
    "INTC" :
        {
            "Company" : "Intel Corp.",
            "Price" : 38.10,
            "Description" : "Intel Corp. engages in the design, manufacture, and sale of computer products and technologies. It delivers computer, networking, data storage, and communications platforms."
        },
    "AAPL" :
        {
            "Company" : "Apple Inc.",
            "Price" : 182.81,
            "Description" : "Apple, Inc. engages in the design, manufacture, and sale of smartphones, personal computers, tablets, wearables and accessories, and other varieties of related services. "
        }
}

json_object = json.dumps(stock)

with open ("stockfile.json", "w") as outfile:
    outfile.write(json_object)

