package com.example.forgerydetection;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONObject;

public class UserComplaints extends AppCompatActivity implements JsonResponse {
    SharedPreferences sh;
    String[] comp,rply,date,val;
    ListView l1;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_user_complaints);

        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());

         l1 = findViewById(R.id.lvcm);
        Button b1 = findViewById(R.id.button10);
        EditText e1 = findViewById(R.id.editTextTextPersonName5);

        JsonReq JR = new JsonReq();
        JR.json_response = (JsonResponse) UserComplaints.this;
        String q = "/viewcomplaints?lid="+sh.getString("log_id","");
        q = q.replace(" ", "%20");
        JR.execute(q);

        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String complaint = e1.getText().toString();
                if (complaint.equalsIgnoreCase("")) {
                    e1.setError("Enter Complaint to Submit");
                    e1.setFocusable(true);
                }else {
                    JsonReq JR = new JsonReq();
                    JR.json_response = (JsonResponse) UserComplaints.this;
                    String q = "/usercomplaints?complaint=" + complaint + "&lid=" + sh.getString("log_id", "");
                    q = q.replace(" ", "%20");
                    JR.execute(q);
                }
            }
        });
    }

    @Override
    public void response(JSONObject jo) {
        try {



            String method = jo.getString("method");
            Log.d("result", method);
//                Toast.makeText(getApplicationContext(), status, Toast.LENGTH_LONG).show();

            if (method.equalsIgnoreCase("usercomplaints")){
                String status = jo.getString("status");
                if (status.equalsIgnoreCase("success")) {


                    Toast.makeText(getApplicationContext(), "Complaint Send Successfull", Toast.LENGTH_SHORT).show();
                    startActivity(new Intent(getApplicationContext(), UserComplaints.class));
                    //startService(new Intent(getApplicationContext(),Notiservise.class));
                }
//

            }
            else if (method.equalsIgnoreCase("viewcomplaints")) {
                String status = jo.getString("status");
                Log.d("result", status);
                Toast.makeText(getApplicationContext(), status, Toast.LENGTH_LONG).show();
                if (status.equalsIgnoreCase("success")) {

                    JSONArray ja = (JSONArray) jo.getJSONArray("data");



                    comp = new String[ja.length()];
                    rply = new String[ja.length()];
                    date = new String[ja.length()];
                    val = new String[ja.length()];


                    for (int i = 0; i < ja.length(); i++) {


                        comp[i] = ja.getJSONObject(i).getString("complaint");
                        rply[i] = ja.getJSONObject(i).getString("reply");
                        date[i] = ja.getJSONObject(i).getString("date");


                        val[i] = "Complaint: " + comp[i]+"\nReply :" + rply[i] + "\nDate: " + date[i]+"\n";
                    }
                    l1.setAdapter(new ArrayAdapter<>(getApplicationContext(), android.R.layout.simple_list_item_1, val));

                }
            }





        } catch (Exception e) {
            e.printStackTrace();
            Toast.makeText(getApplicationContext(), e.toString(), Toast.LENGTH_LONG).show();
        }
    }
    public void onBackPressed()
    {
        // TODO Auto-generated method stub
        super.onBackPressed();
        Intent b=new Intent(getApplicationContext(),UserHome.class);
        startActivity(b);
    }
}