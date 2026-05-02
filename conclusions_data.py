# conclusions_data.py

def get_conclusions():
    """
    Returns a dictionary containing the analytical conclusions and insights
    for each section of the Adalimumab dashboard.
    """
    return {
        "geo_map": """**The main goal was to see how clinical trials for Adalimumab are distributed around the world.**

We used the **ClinicalTrials.gov API (v2)** to pull a live list of studies. After downloading the data, we used Python to clean it up and count the number of trials registered in each country. Then, we used **Plotly** to visualize this on a world map where the size and color of the bubbles represent the "Trial Volume."

**What we see:**
* **The USA is the clear leader.** That massive dark red bubble over North America shows that the overwhelming majority of clinical research for this molecule is concentrated there.
* **Japan is a very strong second.** There is a high density of trials there, even compared to large European nations.
* **Europe is busy but fragmented.** There are a lot of bubbles across Europe, showing constant activity, but individually, they don't reach the scale of the US or Japan in this dataset.
* **Huge "Blank" Areas.** Large parts of the map—like Africa, Central Asia, and most of South America—have almost no recorded trials.

**Our Takeaway:**
Since this is a training study using real-world data, we are simply observing the current landscape. It is clear that R&D is heavily concentrated in a few key global markets, while the rest of the world remains largely "quiet" in terms of clinical trial volume for this specific drug.""",

        "pipeline": """**The main goal was to look at the clinical trial pipeline for Adalimumab and see which companies are running the most studies and at what stage.**

We used the **adalimumab_pipeline_intelligence.csv** dataset to count trials for each sponsor. By breaking them down into clinical phases, we could see where the most effort is being spent—from early Phase 1 tests to late-stage Phase 4 monitoring.

**What we see:**
* **Abbott and AbbVie are at the top.** Their bars are the tallest, showing they have conducted far more trials than anyone else on the list.
* **A sea of red (Phase 3).** For almost every company, the largest part of their bar is red, meaning most of the research activity is concentrated in Phase 3.
* **Pfizer and Eli Lilly are also in the race.** These major companies have significant trial volumes, mostly focused on Phase 3 and Phase 4.
* **Earlier phases are smaller.** Phase 1 and Phase 2 trials (the blue sections) make up a much smaller portion of the total volume for these top sponsors compared to the late-stage research.

**Our Takeaway:**
Looking at these real-world numbers, it is clear that the Adalimumab landscape is dominated by the original manufacturers who have built a massive foundation of clinical data. The high volume of Phase 3 trials across all sponsors shows just how much work goes into testing these drugs before they reach the market.""",

        "clinical_trials": """**Our goal was to combine real clinical trial data from ClinicalTrials.gov with the FDA Purple Book (the official list of approved biologics in the US) and create a visualization.**

First, our script ran through the ClinicalTrials.gov API and pulled all trials involving adalimumab. We collected the trial number, sponsor (who pays for it), phase, start and end dates, and number of patients.

We then loaded purple_book.csv and filtered it by adalimumab to find out which companies already have FDA-approved drugs and, most importantly, which of them are "Interchangeable" (meaning a pharmacist can dispense them instead of the original Humira).

Next, we merged the two tables by sponsor name to understand which trialists ultimately led to an approved product and which are still "In Pipeline" (under development).

**Visualization.** 
* **Gantt Chart:** We've created a timeline of all Phase 3 and 4 trials. The trials that led to the creation of an Interchangeable product are highlighted in green, while all others are highlighted in blue. This allows us to quickly assess who started early and whose path to market was the longest.
* **Scatter Plot:** We compared the trial duration (in months) with the number of patients enrolled. Again, color coding helped us see whether Interchangeable biosimilar trials were larger in scope or duration than others.

**What this tells us:**
Even without in-depth analysis, we can see the scale of the adalimumab race. The green dots and bars (Interchangeable products) show us the winners of this race, who invested time and money in extensive clinical trials (enrollment) to obtain this coveted FDA designation. And the blue bars show how many other companies have tried, or are still trying, to get a piece of this multi-billion dollar pie!""",

        "regulatory": """**The main goal was to track the timeline of FDA approvals for Adalimumab products using data extracted from the official FDA Purple Book.**

We utilized this source as it is considered the definitive reference for biological products in the US. It allowed us to plot the approval dates for all Adalimumab competitors and identify those that achieved **Interchangeable** status.

**What we see:**
* **A 14-year head start.** Humira was approved in late 2002 and remained the sole player in this field for a very long period.
* **The 2016 Breakpoint.** The first biosimilar did not emerge until 14 years later, triggering a subsequent "parade" of new brand entrants.
* **Yellow is the new Black.** Most data points on the chart are yellow, indicating that manufacturers are overwhelmingly pursuing Interchangeable status to facilitate easier pharmacy-level substitution.

**Our Takeaway & Data Note:**
While these data points are official and accurate, it is important to note that this represents only the US market history (FDA). To gain a global perspective, we would need to analyze other regulatory databases, such as the European **EMA** or the Japanese **PMDA**. Additionally, approval dates do not always reflect actual market launch dates due to patent litigation, making this chart just one chapter in a much larger story.""",

        "safety": """**The main goal was to analyze the real-world safety profile of Adalimumab using public adverse event reports.**

We processed a dataset sourced from the **FDA Adverse Event Reporting System (FAERS)**. By cleaning the raw reports and aggregating the "Adverse_Event" counts, we built a treemap to visualize the most common issues reported by patients and healthcare professionals.

**What we see:**
* **Effectiveness Concerns.** "Drug Ineffective" is the single largest category, represented by the darkest red block.
* **Physical Side Effects.** "Pain," "Fatigue," and "Rash" are significant clusters, showing common patient experiences beyond the primary condition.
* **Administrative Reports.** A large portion of reports involve "Off Label Use," highlighting how the drug is being used in clinical practice versus its official indications.

**Our Takeaway & Data Note:**
This analysis is based strictly on **US FDA data**. Much like the regulatory timeline, this is only one part of the story. To see the full global safety profile, we would need to examine other international databases, such as the European **Eudravigilance (EMA)**. Additionally, it is important to remember that these are spontaneous reports; they represent "signals" from the real world rather than results from a controlled clinical environment.""",

        "kol": """**The main goal was to identify leading Key Opinion Leaders (KOLs) for Adalimumab by measuring their academic "Share of Scientific Voice."**

We retrieved this data using the **Europe PMC REST API**, which aggregates millions of publications from **PubMed** and other scientific repositories. By counting how many times an author is linked to Adalimumab research, we can identify who is currently shaping the clinical discourse.

**What we see:**
* **Top Contributors.** Richard B Warren and Lone Skov are the most prominent voices in this dataset.
* **Academic Influence.** The Top 15 list shows a high concentration of research output from a small group of highly active scientists.

**Our Takeaway & Data Note:**
While Europe PMC is a massive source, this mapping has limitations. It only counts publications and doesn't reflect real-world clinical impact or conference speaking roles. To get a full 360-degree view, we would eventually need to integrate other databases like **Google Scholar** or **Scopus** to ensure no influential voices were missed.""",

        "financials": """**The main goal was to analyze manufacturer financial strategies by tracking payments made to healthcare professionals.**

We extracted this data from the **CMS Open Payments (Program Year 2024)** database. Our script filtered millions of records to identify payments specifically linked to Adalimumab, revealing how resources are allocated to influence clinical choice.

**What we see:**
* **High-Volume Engagement.** **Food and Beverage** payments represent the vast majority of interactions (over 99% of transactions in our dataset), indicating a strategy of constant, low-cost engagement at the clinic level.
* **Targeted Influence.** A small number of top-tier experts receive significant sums. For example, **John Cush** leads the list with nearly $190,000 in recorded payments for 2024.
* **Strategic Spending.** Beyond meals, manufacturers invest in **Consulting Fees** and **Speaker Honoraria** to compensate key experts for their professional insights.

**Our Takeaway & Data Note:**
This data highlights a dual-track strategy: high-frequency small payments to maintain presence in local clinics, and large targeted payments to secure the expertise of top leaders. **Note:** This data is specific to the **US market**. For a complete view, international transparency reports (like EFPIA in Europe) would need to be analyzed.""",

        "medicare": """**The main goal was to analyze Medicare spending patterns and product lifecycle management strategies leading up to the 2023 patent cliff.**

We utilized the **CMS Medicare Part D Spending ledger**, which provides a public record of how tax dollars are spent on specific drug formulations. By tracking spending and unit costs over a five-year period, we can see the commercial maneuvers performed by the manufacturer before biosimilars entered the market.

**What we see:**
* **The Citrate-Free (Cf) Transition.** The stacked bar chart shows a massive migration of patients. As spending on the original "Humira Pen" (purple) decreased, spending on the newer "Humira(Cf) Pen" (green) exploded, effectively moving the patient base to a newer formulation.
* **Rising Monopoly Premiums.** The line chart reveals that despite the approaching competition, the average unit cost didn't drop—it climbed from roughly $2,600 to nearly $3,800, a massive increase right before the market opened up.
* **Early Biosimilar Entry.** At the very top of the 2023 bar, we see tiny slivers for the first biosimilars (Amjevita, Cyltezo, etc.), showing they had a very small initial footprint in the Medicare Part D market compared to the brand leader.

**Our Takeaway & Data Note:**
This visualization captures a textbook "product hopping" strategy, where a manufacturer shifts the market to a newer version of a drug to maintain dominance. However, this data has significant limitations: it only reflects **Medicare Part D** spending. It does not account for the massive **commercial (private insurance) market**, Medicare Part B, or international healthcare systems. Furthermore, these figures represent "gross spending" and do not include the confidential rebates that manufacturers pay back to insurance companies, which can significantly change the actual "net" cost.""",

        "wac": """**The goal was to download WAC (Wholesale Acquisition Cost) data and visualize it.**

An Excel spreadsheet with WAC history for 5 years was downloaded from the California Health and Human Services (CHHS) Open Data Portal. This file records specific moments and amounts of price increases for each manufacturer over the past 5 years.

We wrote a script that extracts the pure trade name and manufacturer (for example, Humira (AbbVie)). Next, we created a step line chart.

**What do we see on the chart?**
If you look at the chart, you'll see only one line—Humira from AbbVie—which methodically, like clockwork (every January!), climbs upward.

**Where are all the others? Where are the cheap generics?**
The absence of other companies on this chart isn't a script error, but a characteristic of the market and the data itself. Biosimilars (Humira's competitors) only entered the US market in 2023. First, they entered with prices significantly lower than the original Humira. Second, they simply haven't raised prices yet to be included in this specific "increase" report!

**What do the horizontal lines mean?** 
Plotly draws a vertical line connecting the prices of all the different Humira packages on the day of the increase (January 2021). It takes the last point in this list for 2021 and draws a horizontal blue line from it to the first point in the list for 2022.""",

        "nadac": """**The goal was to download real NADAC data and visualize it.** To do this, we used open data from the US government website (Medicaid.gov). Specifically, we downloaded NADAC database files for 2024, 2025, and 2026. Unlike official company price lists (WAC), the NADAC database shows the actual prices pharmacies pay for medications.

The files we received were quite large JSON archives. To process them, we wrote a custom Python script that read these files in small portions to avoid overloading the computer's memory, found and extracted only those lines that mentioned "adalimumab" or the names of its generics (Humira, Cyltezo, Hadlima, etc.). Next, I cleaned the data, normalized the dates, removed unnecessary information, and created a convenient, compact table (CSV file).

Next, we created an interactive scatter plot using the Plotly library. Each point on the graph represents the recorded price of a specific package of the drug in a given month.

**Looking at the graph, we see that the market is very heterogeneous in terms of prices.** The original drug (Humira) is at the very top. Moreover, we clearly see that the price depends on the concentration: an 80 mg dose costs almost $6,700 per syringe, while 40 mg costs around $3,300.
At the very bottom of the graph, we see generic versions from other companies (Hadlima, Yuflyma, and generics). They sell the same dose (40 mg) for only $600-$1,000!

An interesting paradox: there are drugs on the market with exactly the same composition and dosage (40 mg), but one costs $3,300, and the other $600. How is this possible? As far as I understand, this is due to the peculiarities of the American rebates system, where a high price on paper benefits insurance brokers, while cheaper alternatives are purchased by those paying out of pocket. But I'm still learning the nuances of pricing.""",

        "openfda": """**A brief overview of adalimumab biosimilars in the US.**

The goal was to identify the main manufacturers of adalimumab biosimilars in the US, the concentrations they produce, and how they package the drug.

What we did: we wrote a Python script that directly accesses the openFDA database, which is completely open and free, exactly what we needed for our educational research. For the keyword Adalimumab, we retrieved information from the database in the form of a table with the following fields:

`product_ndc`, `generic_name`, `labeler_name`, `active_ingredients`, `finished`, `packaging`, `listing_expiration_date`, `marketing_category`, `dosage_form`, `spl_id`, `product_type`, `marketing_start_date`, `product_id`, `brand_name_base`, `brand_name`, `route`, `application_number`, `pharm_class`, `openfda.manufacturer_name`, `openfda.rxcui`, `openfda.spl_set_id`, `openfda.is_original_packager`, `openfda.upc`, `openfda.nui`, `openfda.pharm_class_epc` `openfda.pharm_class_moa`, `openfda.pharm_class_cs`, `openfda.unii`

For our current purposes, only the first six fields were selected:
1. `product_ndc`
2. `generic_name`
3. `labeler_name`
4. `active_ingredients`
5. `finished`
6. `packaging`

What did we see? Of course, we saw the manufacturers' names, but more interesting was the "finished" status, which indicates which products are ready for sale to consumers and which are not. A manufacturer can sell prefilled syringes to another company, which in turn completes the packaging and labeling process. Or the manufacturer can sell bags of the drug to other companies, which in turn sterilely fill the drug into syringes and then either label and package them themselves or send them to other companies for packaging and labeling.

Next, we plan to search the internet for similar open databases in the European and Asian markets and create a more comprehensive review."""
    }