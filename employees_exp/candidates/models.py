from django.db import models


class Candidate(models.Model):
    name = models.CharField(max_length=30)

    @property
    def total_experience(self):
        work_experience = WorkExperience.objects.filter(candidate__name=self.name)
        test_exp = work_experience.values()[::1]
        count = []
        for i in test_exp:
            list_of_experience = list(dict.values(i))
            start_work = list_of_experience[1]
            end_work = list_of_experience[2]
            count_experience = end_work - start_work
            count.append(count_experience.days)
            print(list_of_experience)
            print(count)
        total_experience = int(sum(count) / 365)

        # Tests of Experience count :)
        # for i in test_exp:
        #     res = []
        #     x = list(WorkExperience.objects.values(i))
        #     print(x)
        #     for item in x:
        #         print(item)
        #         time_count = datetime.strptime(item, '%b %Y')
        #         res.append(time_count)
        #     current_time_work = res[1] - res[0]
        #     out.append(current_time_work.days)
        # total_experience = int(sum(out) / 365)

        return total_experience

    @property
    def work_experience(self):
        work_experience = WorkExperience.objects.filter(candidate__name=self.name)
        return work_experience

    def __str__(self):
        return self.name


class WorkExperience(models.Model):
    start = models.DateField()
    end = models.DateField()
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
