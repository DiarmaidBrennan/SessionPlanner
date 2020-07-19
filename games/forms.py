from django import forms

from .models import Game

class GameForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = ('name', 'description', 'min_num_players', 'max_num_players',
            'scaleability', 'tech_prof_body_catch', 'tech_prof_punt_kick',
            'tech_prof_pick_up', 'tech_prof_hand_pass', 'tech_prof_hook_kick',
            'tech_prof_near_hand_tackle', 'tech_prof_block', 'tactical_prowess',
            'team_play', 'physical_fitness', 'playing_facts', 'psy_focus',
            'coach_to_player_ratio', 'min_age', 'max_age',)