
from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
	def setUp(self):
		self.team = Team.objects.create(name='Test Team')
		self.user = User.objects.create(name='Test User', email='test@example.com', team=self.team)
		self.activity = Activity.objects.create(user=self.user, type='Running', duration=30)
		self.workout = Workout.objects.create(name='Test Workout', description='Test Desc')
		self.leaderboard = Leaderboard.objects.create(team=self.team, points=10)

	def test_user_creation(self):
		self.assertEqual(self.user.name, 'Test User')
		self.assertEqual(self.user.team.name, 'Test Team')

	def test_activity_creation(self):
		self.assertEqual(self.activity.type, 'Running')
		self.assertEqual(self.activity.duration, 30)

	def test_workout_creation(self):
		self.assertEqual(self.workout.name, 'Test Workout')

	def test_leaderboard_creation(self):
		self.assertEqual(self.leaderboard.points, 10)
