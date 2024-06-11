package com.example.forgerydetection;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class UserPassport extends AppCompatActivity implements JsonResponse {
    public  static String passno;
    TextView t1;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_user_passport);

         t1 = findViewById(R.id.textView9);



        JsonReq JR = new JsonReq();
        JR.json_response = (JsonResponse) UserPassport.this;
        String q = "/viewpassport?pid="+AndroidBarcodeQrExample.contents;
        q = q.replace(" ", "%20");
        JR.execute(q);


    }

    @Override
    public void response(JSONObject jo) {
        try {
            String status = jo.getString("status");
            Log.d("pearl", status);

            if (status.equalsIgnoreCase("success")) {

                String pno = jo.getString("pno");
                passno=pno;
                t1.setText(passno);

            }

        } catch (JSONException e) {

            Toast.makeText(getApplicationContext(), e.toString(), Toast.LENGTH_LONG).show();

        }
    }
}