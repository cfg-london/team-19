import java.io.File;
import java.util.ArrayList;
import java.io.BufferedReader;
import java.util.List;
import java.util.Scanner;
import java.io.FileReader;
import java.io.IOException;


public class NewDemo {
    public static void main(String[] args)
    {
        String csv_path =  "/Users/macbook/Desktop/data.csv";
        File csv_file = new File(csv_path);
        try {
            BufferedReader reader = new java.io.BufferedReader(new java.io.FileReader(csv_file));
            String line = reader.readLine();
            while(line !=null) {
                line = reader.readLine();
                //String[] sequence = line.split(",");
                ArrayList<String> country = new java.util.ArrayList<String>();
                ArrayList<String> year = new java.util.ArrayList<String>();
                System.out.println(line);
                //country.add(sequence[0]);
                //year.add(sequence[1]);

                //System.out.println(country.get(1));
                //System.out.println(year);


                //System.out.println(line);
            }

        }catch(java.io.IOException ex)
        {
            ex.printStackTrace();
        }





        //String input = FileIO.readerToString(is);
        //String input = new String(java.nio.file.Files.readAllBytes(java.nio.file.Paths.get(args[0])));
    }
}
