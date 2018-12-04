from django.shortcuts import render
from recko_api.models import person,universe,family

# Create your views here.

def store_universe(request,name=None):
	try:
		u = universe.objects.create(universe_name=name)
		u.save()
		data = "success"
	except Exception as e:
		data = "already present"
		
	return render(request,"recko/index.html",{"data":data})

def store_family(request,name=None):
	try:
		f = family.objects.create(family_name=name)
		f.save()
		data = "success"
	except Exception as e:
		data = "already present"
	return render(request,"recko/index.html",{"data":data})

def store_person(request,name=None,fid=None,uid=None,power=None):
	try:
		p = person.objects.create(person_name=name,family_id=fid,universe_id=uid,power=power)
		p.save()
		data = "success"
	except Exception as e:
		data = "already present"
	
	return render(request,"recko/index.html",{"data":data})

def list(request,universe=None):
	persons = person.objects.filter(universe_id=universe)
	dict_family = {}
	for p in persons:
		fam_id = p.family_id
		if fam_id not in dict_family:
			dict_family[fam_id] = 1

	# print (dict_family)
	families = family.objects.all()
	# print (families)
	list_fam = []
	for fid in dict_family:
		# print(families[fid-1].family_name)

		list_fam.append(families[fid-1].family_name)
	# print(list_fam)
	return render(request,"recko/index.html",{"data":list_fam})

def power_check(request):
	unbalanced_family = []
	families = family.objects.all()
	for fam in families:
		persons = person.objects.filter(family_id=fam.id)
		universe_dict = {}
		for p in persons:
			p_id = p.universe_id
			if p_id in universe_dict:
				universe_dict[p_id] = universe_dict[p_id] + p.power
			else:
				universe_dict[p_id] = p.power
		flag=0
		if universe_dict :
			check = universe_dict[p_id]
			#print(check)
			for powers in universe_dict:
				#print(universe_dict[powers])
				if(universe_dict[powers]!=check):
					flag=1
					break
		if flag:
			unbalanced_family.append(fam.family_name)
	return render(request,"recko/index.html",{"data":unbalanced_family})

def balance_family(request):
	unbalanced_family = []
	families = family.objects.all()
	for fam in families:
		persons = person.objects.filter(family_id=fam.id)
		universe_dict = {}
		total_power = 0
		for p in persons:
			total_power = total_power + p.power
			p_id = p.universe_id
			if p_id in universe_dict:
				universe_dict[p_id] = universe_dict[p_id] + p.power
			else:
				universe_dict[p_id] = p.power

		flag=0
		print("test")
		print(total_power)
		print(universe_dict)
		count_universe = len(universe_dict)
		if universe_dict :
			check = universe_dict[p_id]
			print(check)
			for powers in universe_dict:
				print(universe_dict[powers])
				if(universe_dict[powers]!=check):
					flag=1
					break
		if flag:
			print(fam.id)
			unbalanced_family.append(fam.family_name)
			if total_power%count_universe == 0:
				equal_power = total_power//count_universe
			else:
				equal_power = total_power//count_universe + count_universe
			for univ in universe_dict:
				pers = persons.filter(universe_id=univ)[0]
				diff_power = equal_power - universe_dict[univ]
				pers.power = pers.power + diff_power
				pers.save()
				print(diff_power)

	return render(request,"recko/balance.html",{"data":unbalanced_family})






