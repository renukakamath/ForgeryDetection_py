package com.example.forgerydetection;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.Preference;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class UserReqPassport extends AppCompatActivity implements JsonResponse {
    SharedPreferences sh;
    public static  String stus;
    TextView t1;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_user_req_passport);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());

        Button b1 = findViewById(R.id.button9);

         t1 = findViewById(R.id.textView5);




        JsonReq JR = new JsonReq();
        JR.json_response = (JsonResponse) UserReqPassport.this;
        String q = "/viewreq?lid="+sh.getString("log_id","");
        q = q.replace(" ", "%20");
        JR.execute(q);

        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                JsonReq JR = new JsonReq();
                JR.json_response = (JsonResponse) UserReqPassport.this;
                String q = "/userreq?lid="+sh.getString("log_id","");
                q = q.replace(" ", "%20");
                JR.execute(q);
            }
        });
    }

    @Override
    public void response(JSONObject jo) {
        try {
            String method = jo.getString("method");
            Log.d("pearl", method);

            if (method.equalsIgnoreCase("userreq")) {


                String status = jo.getString("status");
                if (status.equalsIgnoreCase("success")) {
                    Toast.makeText(getApplicationContext(), "Application Sent Successfully...", Toast.LENGTH_SHORT).show();
                    startActivity(new Intent(getApplicationContext(), UserHome.class));


                } else if (status.equalsIgnoreCase("already")) {
                    Toast.makeText(getApplicationContext(), "Application already Sent.", Toast.LENGTH_SHORT).show();
                    startActivity(new Intent(getApplicationContext(), UserHome.class));


                }

            }
            if (method.equalsIgnoreCase("viewreq")) {

                String stat = jo.getString("status");
                stus=stat;
                t1.setText("Status : "+stus);

            }

        } catch (JSONException e) {

            Toast.makeText(getApplicationContext(), e.toString(), Toast.LENGTH_LONG).show();

        }
    }
}