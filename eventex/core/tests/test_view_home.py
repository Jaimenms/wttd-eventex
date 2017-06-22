from django.test import TestCase
from django.shortcuts import resolve_url as r

class HomeTest(TestCase):
    fixtures = ['keynotes.json']

    def setUp(self):
        self.response = self.client.get(r('home'))

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """GET / must use index.html"""
        self.assertTemplateUsed(self.response, 'index.html')

    def test_subscription_link(self):
        expected = 'href="{}"'.format(r('subscriptions:new'))
        self.assertContains(self.response, expected)

    def test_speakers(self):
        """Must show keynote speakers"""
        contents = [
            'href="{}"'.format(r('speaker_detail', slug='grace-hopper')),
            'href="{}"'.format(r('speaker_detail', slug='alan-turing')),
            "Grace Hopper",
            "http://hbn.link/hopper-pic",
            "Alan Turing",
            "http://hbn.link/turing-pic",
        ]
        for content in contents:
            self.assertContains(self.response, content)

    def test_speakers_link(self):
        expected = 'href="{}#speakers"'.format(r('home'))
        self.assertContains(self.response,expected)