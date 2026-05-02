# sources_data.py

def get_sources_content():
    """Returns the text content and links for the 'Sources' section."""
    return {
        # "intro": "All intelligence presented in this portfolio was extracted programmatically via Python using the following open-source government and academic databases:",
        "sources": [
            {
                "name": "ClinicalTrials.gov (v2 API)",
                "link": "https://clinicaltrials.gov/data-api",
                "description": "Utilized to map global clinical trial footprints and analyze the R&D pipeline for reference biologics and biosimilar competitors."
            },
            {
                "name": "FDA Purple Book",
                "link": "https://purplebooksearch.fda.gov/",
                "description": "The definitive database for biological products, used to track approval timelines, exclusivity periods, and interchangeability designations."
            },
            {
                "name": "openFDA (FAERS & Listings)",
                "link": "https://open.fda.gov/",
                "description": "A comprehensive API platform used to access the FDA Adverse Event Reporting System (FAERS) for safety analysis and Structured Product Labeling (SPL) for inventory insights."
            },
            {
                "name": "Europe PMC REST API",
                "link": "https://europepmc.org/RestfulWebService",
                "description": "An academic repository used to parse scientific literature and quantify the 'Scientific Voice' of Key Opinion Leaders (KOLs) in the pharmaceutical sector."
            },
            {
                "name": "CMS Open Payments",
                "link": "https://openpaymentsdata.cms.gov/",
                "description": "A federal transparency program database used to analyze financial relationships and transfers of value between manufacturers and healthcare providers."
            },
            {
                "name": "CMS Medicare Part D Spending",
                "link": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-spending-by-drug/medicare-part-d-spending-by-drug",
                "description": "Federal spending records used to evaluate lifecycle management strategies and unit cost trajectories for drugs covered under Medicare Part D."
            },
            {
                "name": "CHHS Open Data Portal (WAC)",
                "link": "https://data.chhs.ca.gov/dataset/prescription-drug-wholesale-acquisition-cost-wac-increases",
                "description": "California Health and Human Services data used to track Wholesale Acquisition Cost (WAC) increases and list price transparency."
            },
            {
                "name": "Medicaid.gov (NADAC)",
                "link": "https://data.medicaid.gov/dataset/4a0011dd-3df1-537d-bdde-97ae202b0331",
                "description": "National Average Drug Acquisition Cost (NADAC) data used to analyze real-world pharmacy-level pricing and retail market dynamics."
            }
        ]
    }