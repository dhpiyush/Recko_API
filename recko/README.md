
Steps to follow:
1. Run virtual env . recko_env/bin/activate
2. Move to folder recko ... cd recko
3. python3 manage.py runserver
4. Store universe : http://localhost:8000/store_universe/{universe_name}
   replace universe_name with any name
5. Store family : http://localhost:8000/store_family/{family_name} 
6. Store person : http://localhost:8000/store_person/{person_name}/{family_id}/{universe_id}/{power}
	person_name: string
	family_id : int
	universe_id : int
	power : int
	eg: http://localhost:8000/store_person/piyush/1/1/100
7. List families in a particular universe : http://localhost:8000/list/{universe_id}
	eg: http://localhost:8000/list/3
8. Check if families with same identifiers have same power in all universes: http://localhost:8000/check
9. Find unbalanced families and balance them : http://localhost:8000/balance
