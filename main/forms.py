''' Kind reminders, (please review before editing!)
    - Forms are for validating input, NOT business logic.
    - Only include model specific logic in forms if it is required for input.
      Example: user should be able to select only the groups it is member of.
    '''

from django import forms

from bashoneliners.main.models import OneLiner

''' constants '''

#


''' forms '''

class PostOneLinerForm(forms.ModelForm):
    def save(self, hacker):
	self.instance.hacker = hacker
	return super(PostOneLinerForm, self).save()

    class Meta:
	model = OneLiner

	widgets = {
		'line': forms.Textarea(attrs={'cols': 80, 'rows': 3, }),
		'summary': forms.Textarea(attrs={'cols': 80, 'rows': 3, }),
		'explanation': forms.Textarea(attrs={'cols': 80, 'rows': 10, }),
		'caveats': forms.Textarea(attrs={'cols': 80, 'rows': 3, }),
		}

	fields = (
		'line',
		'summary',
		'explanation',
		'caveats',
		'is_published',
		)


# eof