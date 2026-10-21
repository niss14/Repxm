public class T extends Thread{
    public void run(){
        //acciones del thread
    }

    T t = new T();   //Creacion
    
    t.start();      //Activacion
                        //Existen 2 threads

    t.start();
}

