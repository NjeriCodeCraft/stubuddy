from django.db import models



# Define the models first





class NavbarItem(models.Model):
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=200, help_text="Enter URL or Django reverse URL name")
    icon_class = models.CharField(max_length=50, blank=True, null=True, help_text="Optional: Add an icon class like 'fas fa-key'")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class StudyTip(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text="FontAwesome icon class, e.g., 'fas fa-landmark'")

    def __str__(self):
        return self.title

class Course(models.Model):
    name = models.CharField(max_length=100)
    duration = models.CharField(max_length=50, help_text="Duration (e.g., '2 hours')")
    topics = models.TextField(help_text="Comma-separated topics, e.g., 'Topic 1, Topic 2'", blank=True)

    def get_topics(self):
        """Return topics as a list."""
        return [topic.strip() for topic in self.topics.split(",") if topic.strip()]

    def __str__(self):
        return self.name

class Sign_in(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name