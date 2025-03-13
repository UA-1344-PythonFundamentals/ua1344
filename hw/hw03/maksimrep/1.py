import this
import codecs

p = codecs.decode(this.s, 'rot13')

print("\n", "Better =" , p.lower().count("better"))
print("Never =" ,p.lower().count("never"))
print ("Is = " ,p.lower().count("is"))

print("\nUppercase text:\n", p.upper())
print("\nModified text:\n", p.replace("I", "&"))
