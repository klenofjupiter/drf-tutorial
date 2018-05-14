from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

# class SnippetSerializer(serializers.Serializer):
# 	""" this part defines which fields get serialized/deserialized (sent or not sent)"""
# 	id = serializers.IntegerField(read_only=True)
# 	title = serializers.CharField(required=False, allow_blank=True, max_length=100)
# 	code = serializers.CharField(style={'base_template': 'textarea.html'})
# 	linenos = serializers.BooleanField(required=False)
# 	language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
# 	style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

# 	def create(self, validated_data):
# 		""" create and return a new snippet, assuming data validates """
# 		return Snippet.objects.create(**validated_data)

# 	def update(self, instance, validated_data):
# 		""" update and return an existing 'snippet' instance given the validated data """ 
# 		instance.title = validated_data.get('title', instance.title)
# 		instance.code = validated_data.get('code', instance.code)
# 		instance.linenos = validated_data.get('linenos', instance.linenos)
# 		instance.language = validated_data.get('language', instance.language)
# 		instance.style = validated_data.get('style', instance.style)
# 		instance.save()
# 		return 


## this version below allows us to not repeat code that is already essentially written in our models file, 
## and gives us simple default implementations of create and update methods 

class SnippetSerializer(serializers.ModelSerializer):
	class Meta:
		model = Snippet
		fields = ('id', 'title', 'code', 'linenos', 'language', 'style')