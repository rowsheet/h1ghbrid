curl -i \
	-H "Accept: application/json" \
	-H "X-HTTP-Method-Override: PUT" \
	-X POST -d "\"{\
'HELLO': 'bitch'\
}\"" \
	http://localhost:8000/public_api/
