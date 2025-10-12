import java.io.*;
import java.net.Socket;

public class ClientHttp 
{
    public static void main(String[] args) 
    {
        if (args.length < 1) 
        {
            System.out.println("Usage : java ClientHttp <hote>   (ex: www.univ-rouen.fr)");
            return;
        }
        String host = args[0];

        try (Socket socket = new Socket(host, 80);
             // writers
             OutputStreamWriter osw = new OutputStreamWriter(socket.getOutputStream());
             BufferedWriter bufOut = new BufferedWriter(osw);
             // readers
             InputStreamReader isr = new InputStreamReader(socket.getInputStream());
             BufferedReader bufIn = new BufferedReader(isr)) 
             {

            // Requête HTTP minimale (comme dans le TP)
            String request = "GET / HTTP/1.0\r\n\r\n";
            bufOut.write(request, 0, request.length());
            bufOut.flush();

            // Lecture ligne par ligne (en-têtes + corps si non binaire)
            String line = bufIn.readLine();
            while (line != null) {
                System.out.println(line);
                line = bufIn.readLine();
            }

        } 
        catch (IOException e) 
        {
            System.err.println("Erreur : " + e.getMessage());
        }
    }
}
