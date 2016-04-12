init:
	pip install -r requirements.txt

run: federal-deputy-agencies senate-commission parties
	@echo "Running all scripts"

federal-deputies:
	cd ./data-collection/ && python federal_deputies.py

federal-deputy-agencies: federal-deputies
	cd ./data-collection/ && python federal_deputy_agencies.py

senators:
	cd ./data-collection/ && python senators.py

senate-commission: senators
	cd ./data-collection/ && python senate_commissions.py

parties:
	cd ./data-collection/ && python parties.py
