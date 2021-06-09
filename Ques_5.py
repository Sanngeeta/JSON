# Q5.Json string ko check karo ki bo complex object contain karti hai ya nahi?

# import json
import json
def encode_complex(z):
    if isinstance(z, complex):
        print(type(z))
        return ("real",z.real, "imag",z.imag)
    json.dumps(k,file,indent=3)
print(encode_complex(10+3j))
