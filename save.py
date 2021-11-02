import csv

def save_to_file(jobs):
  file = open("jobs.csv", mode="w")
  writer = csv.writer(file)
  writer.writerow(["title", "company", "location", "link"])
  for job in jobs:
    writer.writerow(list(job.values())) #dictionary로 만들었기 때문에 values만 가져오는 게 가능하다. but 출력시 dict_values 등 거추장스러운 것들 이 붙기 때문에 list로 만들어주자.
  return