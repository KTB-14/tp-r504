import java.io.DataInputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class ServeurTCP1 
{
    public static void main(String[] args) 
    {
        try (ServerSocket socketserver = new ServerSocket(2016)) 
        {
            System.out.println("serveur en attente");

            try (Socket socket = socketserver.accept();
                 DataInputStream dIn = new DataInputStream(socket.getInputStream())) 
                 {

                System.out.println("Connection d’un client");
                String msg = dIn.readUTF();
                System.out.println("Message : " + msg);
            }

        } 
        catch (IOException e) 
        {
            System.err.println("Erreur serveur : " + e.getMessage());
        }
    }
}
