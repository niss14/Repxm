int main(){
    int result;
    int number;

    result = sum(number);

}

int sum(int n){
    if (n!=0)
        return n + sum(n-1);
}

int sum(int n){
    if (n!=0)
        return n + sum(n-1);
    else
        return n;
}