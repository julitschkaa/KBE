swagger: */serializers.py */views.py
	TAX_CALC_API_URL="http://localhost:8000/" python manage.py generateschema --settings='products_service_api.settings' --file=open_api_products_service.yml
	python manage.py generateschema --settings='tax_calc_api.settings' --file=open_api_tax_calc_service.yml

migrate:
	TAX_CALC_API_URL="http://localhost:8000/" python manage.py migrate --settings='products_service_api.settings'
