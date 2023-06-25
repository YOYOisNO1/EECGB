def program169():
    {
     "cells": [
      {
       "cell_type": "code",
       "execution_count": 4,
       "metadata": {},
       "outputs": [
        {
         "name": "stdout",
         "output_type": "stream",
         "text": [
          "5\n",
          "3\n",
          "5\n",
          "4\n"
         ]
        }
       ],
       "source": [
        "b=int(input())\n",
        "g=int(input())\n",
        "n=int(input())\n",
        "ans=n+1\n",
        "for i in range(n+1):\n",
        "    if b<i:\n",
        "        ans=ans-1\n",
        "    elif g<n-i:\n",
        "        ans=ans-1\n",
        "print(ans)"
       ]
      },
      {
       "cell_type": "code",
       "execution_count": null,
       "metadata": {},
       "outputs": [],
       "source": []
      }
     ],
     "metadata": {
      "kernelspec": {
       "display_name": "py36test",
       "language": "python",
       "name": "py36test"
      },
      "language_info": {
       "codemirror_mode": {
        "name": "ipython",
        "version": 3
       },
       "file_extension": ".py",
       "mimetype": "text/x-python",
       "name": "python",
       "nbconvert_exporter": "python",
       "pygments_lexer": "ipython3",
       "version": "3.7.4"
      }
     },
     "nbformat": 4,
     "nbformat_minor": 2
    }