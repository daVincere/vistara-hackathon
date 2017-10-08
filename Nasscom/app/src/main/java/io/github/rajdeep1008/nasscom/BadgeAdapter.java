package io.github.rajdeep1008.nasscom;

import android.content.Context;
import android.content.Intent;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;

import java.util.List;

/**
 * Created by rajdeep1008 on 8/10/17.
 */

public class BadgeAdapter extends RecyclerView.Adapter<BadgeAdapter.ViewHolder> {

    List<Badge> mBadges;
    Context mContext;

    public BadgeAdapter(List<Badge> mBadges, Context mContext) {
        this.mBadges = mBadges;
        this.mContext = mContext;
    }

    @Override
    public ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        Context context = parent.getContext();
        LayoutInflater inflater = LayoutInflater.from(context);

        View contactView = inflater.inflate(R.layout.single_item, parent, false);
        ViewHolder viewHolder = new ViewHolder(contactView);

        return viewHolder;
    }

    @Override
    public void onBindViewHolder(ViewHolder holder, int position) {
        Badge badge = mBadges.get(position);

        ImageView imageView = holder.badgeView;
        imageView.setImageResource(badge.getId());
    }

    @Override
    public int getItemCount() {
        return mBadges.size();
    }

    public class ViewHolder extends RecyclerView.ViewHolder {

        public ImageView badgeView;

        public ViewHolder(View itemView) {
            super(itemView);
            badgeView = (ImageView) itemView.findViewById(R.id.badge_view);
            badgeView.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    mContext.startActivity(new Intent(mContext, MainActivity.class));
                }
            });
        }
    }
}
