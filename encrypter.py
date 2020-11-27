class Encrypter:

    def encrypt(string, show=True):
            result = []

            for char in string:
                val = ord(char) - 18
                result.append(val)

            if show is True:
                for number in result:
                    print(number, end='')
                    print(" ", end='')
            return result

    def decrypt(sequence, show=True):
        result = ""
        for number in sequence:
            val = int(number)
            val = val + 18
            val = chr(val)
            result = result + val

        if show is True:
            print(result)

        return result



