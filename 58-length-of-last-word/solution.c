int lengthOfLastWord(char *s) {

    int i = strlen(s) - 1;

    while (i >= 0 && s[i] == ' ')
        i--;

    int c = 0;

    while (i >= 0 && s[i] != ' ') {
        c++;
        i--;
    }

    return c;
}