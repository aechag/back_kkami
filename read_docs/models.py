from io import BytesIO

from django.db import models
from gtts import gTTS
from django.core.files import File
import tempfile


class doc(models.Model):
    id = models.AutoField(primary_key=True)
    path = models.CharField(max_length=1000)
    nbr_page_read = models.IntegerField(default=0)


    def __str__(self):
        return  ' id : ' + str(self.id) + ' / path : ' + self.path + ' / nbrpageread : ' + str(self.nbr_page_read)


class Audio(models.Model):
    name = models.CharField(max_length=50)
    num_pdf = models.IntegerField()
    audio = models.FileField(null=True, blank=True, upload_to='audios/')
  # audio_file = models.FileField(upload_to='media/uploads', null=False)

  # def save(self,*args, **kwargs):
  #     audio = gTTS(text=self.word_vocab, lang='en', slow=True)
  #
  #     with tempfile.TemporaryFile(mode='w') as f:
  #         audio.write_to_fp(f)
  #         file_name = '{}.mp3'.format(self.word_vocab)
  #         self.audio.save(file_name, File(file=f))
  #
  #     super(Word, self).save(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #   #new_string = str(self.name)
    #   file_name = '{}.mp3'.format(str(self.name).lower().replace(' ', '_'))
    #   #make_sound = gTTS(text=new_string, lang='en')
    #   mp3_fp = BytesIO()
    #   #make_sound.write_to_fp(mp3_fp)
    #   self.audio.save(file_name, mp3_fp, save=False)
    #   super(Audio, self).save(*args, **kwargs)