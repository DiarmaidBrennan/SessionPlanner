from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
class Game(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    min_num_players = models.IntegerField(default=0)
    max_num_players = models.IntegerField(default=0)
    scaleability = models.IntegerField(default=0)
    contact = models.BooleanField(default=False)
    tech_prof_body_catch = models.IntegerField(default=0)
    tech_prof_punt_kick = models.IntegerField(default=0)
    tech_prof_pick_up = models.IntegerField(default=0)
    tech_prof_hand_pass = models.IntegerField(default=0)
    tech_prof_hook_kick = models.IntegerField(default=0)
    tech_prof_near_hand_tackle = models.IntegerField(default=0)
    tech_prof_block = models.IntegerField(default=0)
    tactical_prowess = models.IntegerField(default=0)
    team_play = models.IntegerField(default=0)
    physical_fitness = models.IntegerField(default=0)
    playing_facts = models.IntegerField(default=0)
    psy_focus = models.IntegerField(default=0)
    coach_to_player_ratio = models.IntegerField(default=0)
    min_age = models.IntegerField(default=0)
    max_age = models.IntegerField(default=0)
    num_footballs = models.IntegerField(default=0)
    difficult_rating = models.IntegerField(default=0)
    