import uuid
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
	class Meta:
		unique_together = ('email', )
		verbose_name = 'Account'
		verbose_name_plural = 'Accounts'

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	email = models.EmailField(unique=True)
	is_verified = models.BooleanField(default=False)

	def send_verification_email(self, subject, message, **kwargs):
		"""
        Send an email to this User.
        """
		from_email = 'talhamalik25.tm@gmail.com'
		# Create a plain text version of the email
		text_message = strip_tags(message)

		# Create the EmailMultiAlternatives object
		email = EmailMultiAlternatives(
			subject=subject, body=message, to=[self.email], from_email=from_email, **kwargs
		)
		email.attach_alternative(message, "text/html")


		email.send(fail_silently=False)
		# send_mail(
		# 	subject,
		# 	message,
		# 	'talhamalik25.tm@gmail.com',
		# 	[self.email],
		# 	fail_silently=False,
		# )

	def __str__(self):
		return self.email


class Profile (models.Model):
	def user_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
		return 'user_{0}/profile_pictures/{1}'.format(instance.user.username, filename)

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	estate_name = models.CharField(max_length=256, null=True, blank=True, help_text="Optional")
	phone_number = PhoneNumberField(help_text=_('+92-3211234567'))
	bio_info = models.TextField(max_length=1000, null=True, blank=True, help_text="Optional")
	profile_image = models.ImageField(upload_to = user_directory_path, blank=True)

	def save(self, *args, **kwargs):
		if self.profile_image:
			img = PillowImage.open(self.profile_image)

			# Resize image
			if img.height > 500 or img.width > 500:
				output_size = (500, 500)
				img.thumbnail(output_size)

				# Save the resized image to a BytesIO buffer
				output_buffer = BytesIO()
				img.save(output_buffer, format='JPEG')
				output_buffer.seek(0)

				# Save the buffer content to the image field
				self.profile_image.save(self.profile_image.name, ContentFile(output_buffer.read()), save=False)

		super().save(*args, **kwargs)

	def __str__(self):
		return ""
