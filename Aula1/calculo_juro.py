{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "3cea1b42-5013-4305-8491-10e406f22aa0",
   "metadata": {
    "editable": true,
    "slideshow": {
     "slide_type": ""
    },
    "tags": []
   },
   "source": [
    "## Variáveis\n",
    "\n",
    "- tempo\n",
    "- taxa\n",
    "- capital\n",
    "- juro\n",
    "\n",
    "## Fórmula de cálculo\n",
    "\n",
    "juro = capital.taxa.tempo\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "50f038f5-d4ad-4747-b30b-49d03f214af1",
   "metadata": {},
   "outputs": [],
   "source": [
    "## Entrada de dados\n",
    "\n",
    "tempo = 3\n",
    "capital = 15\n",
    "taxa = 0.1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "4d6bafc3-8079-4af5-a79a-324082c6398d",
   "metadata": {},
   "outputs": [],
   "source": [
    "## Processamento de dados\n",
    "\n",
    "juro = capital*taxa*tempo"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "37da74d3-ca6b-481c-aab0-856fe3d1330e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4.5\n"
     ]
    }
   ],
   "source": [
    "## Saída de dados\n",
    "\n",
    "print(juro)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "855e371b-c98a-4779-9fe1-c0a185f3a73e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
